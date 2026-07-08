### WSL2 Webcam Passthrough Setup (Troubleshooting Guide)
The original tutorial this project is based on assumes the webcam is directly available to OpenCV (cv2.VideoCapture(0)), which is true on native Windows or native Linux. This project instead runs inside WSL2, which by default has no access to USB devices such as webcams. There is nothing to fix in Python or OpenCV here, the device simply isn't visible to the Linux side at all until it's explicitly passed through from Windows.

This document exists so that anyone else re-running this project under WSL2 doesn't have to rediscover this from scratch. If you're running natively on Windows or Linux (not WSL2), you can skip this file entirely.

#### Prerequisites
- Windows 10 (build 21H2+) or Windows 11, with WSL2 already installed.
- Administrator access to Windows (needed for a few one-time setup steps).
- A USB webcam (this was tested with an external UGREEN USB camera; a laptop's built-in camera may behave differently).

#### Step 1: Update WSL (Administrator PowerShell window)
```bash
wsl --update
wsl --shutdown
```
#### Step 2: Install usbipd-win (Administrator PowerShell window)
```bash
winget install --interactive --exact dorssel.usbipd-win
```
#### Step 3: Find the camera's Bus ID (Administrator PowerShell window)
```bash
usbipd list
```

#### Step 4: Bind the camera (Administrator PowerShell window)
```bash
usbipd bind --busid 1-2
```
(Replace 1-2 with whatever BUSID your camera showed in Step 3)

#### Step 5: Attach the camera to WSL (Normal PowerShell window)
```bash
usbipd attach --wsl --busid 1-2
```
> [!IMPORTANT]
> This `attach` step is not permanent. It must be repeated every time WSL is restarted or the camera is unplugged/replugged.

#### Step 6:  Confirm the device is visible inside WSL (WSL)
```bash
sudo apt update
sudo apt install -y usbutils v4l-utils
lsusb
ls -l /dev/video*
```

`lsusb` should list the camera. At this point, `/dev/video*` may or may not already exist, see [Problem 1](#p1) below.

#### Step 7:  Work out which device index is the actual camera (WSL)
```bash
v4l2-ctl --device=/dev/video0 --all
v4l2-ctl --device=/dev/video1 --all
```

#### Step 7:  Work out which device index is the actual camera (WSL)
```bash
v4l2-ctl --device=/dev/video0 --all
v4l2-ctl --device=/dev/video1 --all
```

#### Step 8:  Test the capture in Python (included in the notebook)
```bash
import cv2

cap = cv2.VideoCapture("/dev/video0")  # use whichever index Step 7 identified
ret, frame = cap.read()
print("capture successful:", ret, "frame shape:", frame.shape if ret else None)
cap.release()
```
Once this returns a valid frame, the webcam capture cells in the main notebook (anchor/positive image collection) work as in the original tutorial.

#### Problem 1: `/dev/video0` / `/dev/video1` don't exist <a name="p1"></a>

#### Problem 2:  Permission denied on  `/dev/video*`
