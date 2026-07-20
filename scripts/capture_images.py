"""
capture_images.py

Standalone anchor/positive image capture script — run this on NATIVE WINDOWS
(not inside WSL). It exists purely as a workaround for the WSL2 webcam
passthrough issues documented in WSL_WEBCAM_SETUP.md: OpenCV inside WSL2 could
not reliably open /dev/video0 (see the notebook's debug cells in section 2.2),
so instead of fighting the USB/IP passthrough, image capture is done natively
where the webcam "just works", and the resulting files are copied into the
WSL project folder afterwards.

Usage (in a plain Windows PowerShell / cmd prompt, NOT WSL):

    pip install opencv-python
    python capture_images.py

Controls while the preview window is open:
    a  -> save current frame as an ANCHOR image
    p  -> save current frame as a POSITIVE image
    q  -> quit

Output:
    ./captured/anchor/*.jpg
    ./captured/positive/*.jpg

After capturing, copy these two folders' contents into your WSL project at:
    data/anchor/
    data/positive/

The easiest way to copy them over is through the WSL network path, e.g.:
    \\wsl$\<your-distro-name>\home\<user>\<project-folder>\data\anchor
(Replace <your-distro-name> and the path with your actual WSL distro name
and project location — check with `wsl -l -v` and `pwd` inside WSL.)
"""

import os
import uuid
import cv2

ANCHOR_DIR = os.path.join("captured", "anchor")
POSITIVE_DIR = os.path.join("captured", "positive")

CROP_Y, CROP_X, CROP_SIZE = 120, 200, 250  # matches the crop used in the main notebook


def ensure_dirs():
    try:
        os.makedirs(ANCHOR_DIR, exist_ok=True)
        os.makedirs(POSITIVE_DIR, exist_ok=True)
    except OSError as error:
        raise RuntimeError(f"Could not create output folders: {error}") from error


def main():
    ensure_dirs()

    cap = cv2.VideoCapture(0)  # native Windows: default device index works directly
    if not cap.isOpened():
        raise RuntimeError(
            "Could not open the webcam (index 0). Check that no other "
            "application (Zoom, Teams, etc.) is currently using it, and "
            "that Windows camera privacy settings allow desktop apps access."
        )

    print("Webcam opened. Press 'a' for anchor, 'p' for positive, 'q' to quit.")

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret or frame is None:
                print("Warning: failed to read a frame, retrying...")
                continue

            # Crop to a consistent 250x250 region, same as the original notebook workflow
            cropped = frame[CROP_Y:CROP_Y + CROP_SIZE, CROP_X:CROP_X + CROP_SIZE, :]

            cv2.imshow("Image Collection (a=anchor, p=positive, q=quit)", cropped)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("a"):
                path = os.path.join(ANCHOR_DIR, f"{uuid.uuid1()}.jpg")
                if not cv2.imwrite(path, cropped):
                    print(f"Warning: failed to write {path}")
                else:
                    print(f"Saved anchor: {path}")

            elif key == ord("p"):
                path = os.path.join(POSITIVE_DIR, f"{uuid.uuid1()}.jpg")
                if not cv2.imwrite(path, cropped):
                    print(f"Warning: failed to write {path}")
                else:
                    print(f"Saved positive: {path}")

            elif key == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

    print("Done. Copy the 'captured/anchor' and 'captured/positive' folders "
          "into your WSL project's data/anchor and data/positive folders.")


if __name__ == "__main__":
    main()