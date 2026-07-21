# Facial Recognition System

This repository contains a facial verification system developed for the **Advanced Topics – Introduction to Biometrics** module at HTW Berlin. The implementation uses a Siamese neural network to compare two face images and estimate whether they belong to the same person.

The project includes data collection, preprocessing, model construction, training, evaluation, model saving, and real-time verification using OpenCV.

# Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Data](#data)
4. [Installation](#installation)
5. [Results](#results) 
6. [Known Issues & Workarounds](#issues) 
7. [Acknowledgement](#acknowledgement)
8. [References](#references)

## 1. Introduction  <a name="introduction"></a>

### 1.1 Project Purpose 

The aim of this project is to build and evaluate a facial verification system based on a Siamese neural network.

Unlike a conventional multi-class classifier, the model does not directly predict a person's identity. Instead, it receives two images and learns whether the images represent the same person. This is a form of one-shot learning: rather than requiring many labeled examples per class (per person), the network only needs to learn a general notion of "similarity" between two face images, so a person can be verified from very few (in principle, a single) reference image.

The notebook follows this workflow:

1. Configure the Python and TensorFlow environment.
2. Create anchor, positive, and negative image datasets.
3. Preprocess images into a consistent format.
4. Build an embedding network.
5. Compare image embeddings using an L1 distance layer.
6. Train the Siamese network using binary cross-entropy.
7. Evaluate the model using classification metrics.
8. Save the trained model.
9. Perform real-time facial verification using a webcam.

### 1.2 Theoretical Background
Siamese networks address verification as a similarity learning problem rather than a classification problem. Two identical (weight-sharing) embedding networks map each input image into a fixed-length feature vector; the L1 distance between the two vectors is then passed through a single dense layer with a sigmoid activation to produce a same/different probability. Because the network learns a general notion of similarity rather than fixed per-person classes, it generalizes to identities never seen during training, a person can be verified from as little as one reference (anchor) image, which is why this approach is described as one-shot learning.

Training relies on triplets of images: an anchor, a positive (same identity as the anchor), and a negative (different identity). The network is trained with binary cross-entropy over anchor–positive and anchor–negative pairs, pushing embeddings of the same identity closer together and embeddings of different identities further apart.

This project's architecture and training procedure follow Koch, Zemel, and Salakhutdinov (2015) [4], which introduced this convolutional Siamese approach for one-shot image recognition.

## 2. Requirements <a name="requirements"></a>

The project was developed and tested with the following environment:

- Python 3.7
- TensorFlow 2.4.1
- OpenCV
- NumPy
- Matplotlib
- Jupyter Notebook
- NVIDIA GPU support through WSL2
- CUDA 11.0
- cuDNN 8.0

The project can also run on the CPU, although training and inference may be slower.

### 2.1 Development Environment
This project was developed and tested on the following setup:
| Component | Specification | 
|---|---| 
| Host OS | Windows 11 with WSL2 | 
| WSL2 distribution | Ubuntu 22.04 | 
| GPU | NVIDIA GeForce RTX 3050 Laptop GPU, 4 GB VRAM | 
| CPU | Intel Core i7-10870H, 2.20 GHz | 

## 3. Data <a name="data"></a>

The project uses three image categories:

- **Anchor images:** reference images of the target person.
- **Positive images:** additional images of the same person.
- **Negative images:** images of other people.

> [!IMPORTANT]
> The notebook resizes images to `100 × 100` pixels and scales pixel values to the range `[0, 1]`.

### 3.1 Negative Images: Labeled Faces in the Wild (LFW)

1. Go to Kaggle and log in to your account, or create a new account.
2. Open the [Labeled Faces in the Wild (LFW)](https://www.kaggle.com/datasets/atulanandjha/lfwpeople) dataset page.
3. Download the `lfw-funneled.tgz` file.
4. Move the downloaded file in the same folder as the jupyter notebook.

### 3.2 Anchor & Positive Images: Webcam Capture  <a name="imagesissues"></a>

Anchor and positive images are captured live from the notebook using `OpenCV (cv2.VideoCapture)`, with a key-press workflow (a = save anchor frame, p = save positive frame, q = quit). On a native Windows or Linux installation this works out of the box.

This project runs inside WSL2, where, even after passing the USB webcam through from Windows (see [WSL_WEBCAM_SETUP.md](WSL_WEBCAM_SETUP.md)), cv2.VideoCapture still failed to reliably open the device for live capture. Rather than spend the project time fighting USB/IP passthrough further, the anchor/positive capture step was moved out of WSL entirely:
  1. Run [capture_images.py](scripts/capture_images.py) in a plain Windows Python environment (not WSL). A separate, minimal Python environment on native Windows is needed:

  ```bash
    pip install opencv-python
  ```
  2. This opens the webcam natively, applies the same 250×250 crop used elsewhere in the pipeline, and saves images to captured/anchor/ and captured/positive/ on the Windows side.
  3. Copy the contents of those two folders into the project's data/anchor/ and data/positive/ folders inside WSL.

If you're running this project natively on Windows or Linux (not WSL2), you can ignore this workaround and use the original in-notebook webcam capture cells instead, they are kept in the notebook (commented out) for reference.

### 3.3 Final Dataset Size

The anchor/positive images used for this submission are not included in this repository for privacy reasons.
To reproduce this project with your own data, follow the capture workflow in Section 3.2 to populate `data/anchor` and `data/positive` yourself.

After running the capture and folder-check steps described above, the final counts used for this submission were:

- Anchor images: 443
- Positive images: 458

This falls within the recommended range for this Siamese network setup (roughly 250–400+ per category), giving the model enough variety to learn a stable similarity metric.

## 4. Installation <a name="installation"></a>

### 4.1 Clone the repository

```bash
git clone <repository-url>
cd facial-recognition-system
```

###  4.2 Create the environment from `environment.yml`
The recommended way to install the project is with Conda using the provided `environment.yml` file. This creates an environment with the required Python, TensorFlow, CUDA, cuDNN, OpenCV, Matplotlib, and Jupyter versions.

```bash
conda env create -f environment.yml
conda activate facial-recognition
```

[MANUAL_INSTALLATION.md](MANUAL_INSTALLATION.md): Use this method only when the environment file cannot be used. 

### 4.3 Register the Jupyter kernel

```bash
python -m ipykernel install --user \
  --name facial-recognition \
  --display-name "Python 3.7 - Facial Recognition"
```

### 4.4 Run the project

```bash
conda activate facial-recognition
```

### 4.5 Start Jupyter Notebook

```bash
jupyter notebook
```
Select the kernel: Python 3.7 - Facial Recognition

### 4.6 Usage

1. Run the notebook top to bottom (Sections 1–7) to train and save the model, or skip training by loading the saved `siamesemodelv2.h5` if available (see Section 7).
2. Populate `application_data/verification_images/` with a few reference photos of the enrolled person.
3. Capture (or copy) a test photo as `application_data/input_image/input_image.jpg`.
4. Run `verify(siamese_model, 0.5, 0.5)` (Section 8.1) to check whether the test photo matches the enrolled person.

## 5. Results <a name="results"></a>

- adapting the environment for WSL2: `WSL_WEBCAM_SETUP.md` & moving anchor/positive image capture to a native-Windows script (`capture_images.py`) due to unresolved WSL2 webcam limitations
- Training time: ~4.5 minutes for 50 epochs (model converged by ~epoch 5)
- Precision / Recall on held-out test set: 1.0 / 1.0
- See Section 9 of the notebook for genuine-match and impostor-rejection verification tests.

## 6. Known Issues & Workarounds <a name="issues"></a>

- Some environments display a NUMA-support warning when TensorFlow initializes the GPU. This warning is harmless as long as `tf.config.list_physical_devices("GPU")` returns a GPU and training runs successfully.
- WSL2 has no native USB webcam access. `cv2.VideoCapture` cannot see any camera until it is explicitly passed through from Windows via usbipd-win, and even after passthrough, this project still encountered failures opening the device for a stable live capture session inside WSL2 (`RuntimeError: Could not open /dev/video0`, reproducible in the notebook's own debug cells in Section 2.2). Workaround adopted for this submission: anchor and positive images were captured using [capture_images.py](scripts/capture_images.py) run natively on Windows, then copied into `data/anchor` `/ data/positive`. See [3.2](#imagesissues)
- The same limitation applies to the real-time verification step at the end of the notebook (Section 8). If live verification inside WSL is not possible in your environment either, use the same native-Windows approach to capture a single verification frame and load it into the notebook's `verify()` function as a static image instead of a live `cv2.VideoCapture` loop.
- **Single-identity verification**: like the original tutorial, this implementation verifies against one enrolled person. Supporting multiple enrolled identities would require separate positive-image folders per subject and an updated labeling scheme, rather than the current single anchor/positive structure.
- **Enhanced performance measurement**: this implementation reports precision and recall on the held-out test set (Section 6), but does not compute FNMR/FMR, a DET curve, or a genuine/impostor score histogram. This would be a natural next step for a deeper evaluation.


## 7. Acknowledgement <a name="acknowledgement"></a>

This implementation is adapted from the facial recognition tutorial by **Nicholas Renotte**, which demonstrates a Siamese neural network for facial verification using TensorFlow and OpenCV.

The original tutorial structure and core implementation ideas include:

- collecting anchor and positive images with OpenCV
- using LFW images as negative examples
- creating image pairs with TensorFlow datasets
- building a shared embedding network
- implementing a custom L1 distance layer
- training a Siamese network
- evaluating precision and recall
- performing real-time verification

## 8. References <a name="references"></a>

[1] Nicholas Renotte (2021): Build a Deep Facial Recognition App from Paper to Code Youtube Tutorial: https://www.youtube.com/watch?v=bK_k7eebGgc&list=PLgNJO2hghbmhHuhURAGbe6KWpiYZt0AMH <br>
[2] JUPYTER NOTEBOOKS OF NICHOLAS RENOTTE: https://github.com/nicknochnack/FaceRecognition/tree/main <br>
[3] DATASET: https://www.kaggle.com/datasets/atulanandjha/lfwpeople <br>
[4] Koch, Gregory, Richard Zemel, and Ruslan Salakhutdinov (2015): Siamese neural networks for one-shot image: https://www.cs.utoronto.ca/~rsalakhu/papers/oneshot1.pdf <br>