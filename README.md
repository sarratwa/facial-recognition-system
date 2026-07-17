# Facial Recognition System

This repository contains a facial verification system developed for the **Advanced Topics – Introduction to Biometrics** module at HTW Berlin. The implementation uses a Siamese neural network to compare two face images and estimate whether they belong to the same person.

The project includes data collection, preprocessing, model construction, training, evaluation, model saving, and real-time verification using OpenCV.

# Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Data](#data)
4. [Installation](#installation)
5. [Acknowledgement](#acknowledgement)
6. [References](#references)

## 1. Project Purpose  <a name="introduction"></a>

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

--todo: Add notes on any machine-specific quirks encountered

## 3. Data <a name="data"></a>

The project uses three image categories:

- **Anchor images:** reference images of the target person.
- **Positive images:** additional images of the same person.
- **Negative images:** images of other people.

> [!IMPORTANT]
> The notebook resizes images to `100 × 100` pixels and scales pixel values to the range `[0, 1]`.

Acquiring the negative data was a standard dataset download (Section 3.1). Acquiring the anchor/positive data via webcam was not straightforward, because this project runs inside WSL2, which does not expose USB devices such as webcams to Linux by default. Getting webcam capture working under WSL2 is one of the adaptations this project makes to the original tutorial (see Acknowledgement); the full debugging process is written up separately in [WSL_WEBCAM_SETUP.md](WSL_WEBCAM_SETUP.md) so it doesn't clutter this README, and can be skipped entirely by anyone not running under WSL2.

### 3.1 Negative Images: Labeled Faces in the Wild (LFW)

1. Go to Kaggle and log in to your account, or create a new account.
2. Open the [Labeled Faces in the Wild (LFW)](https://www.kaggle.com/datasets/atulanandjha/lfwpeople) dataset page.
3. Download the `lfw-funneled.tgz` file.
4. Move the downloaded file in the same folder as the jupyter notebook.

### 3.2 Anchor & Positive Images: Webcam Capture

Anchor and positive images are captured live from the notebook using OpenCV (cv2.VideoCapture), with a key-press workflow (a = save anchor frame, p = save positive frame, q = quit).

On a native Windows or Linux installation this works without any extra setup. Under WSL2, cv2.VideoCapture cannot see the webcam at all until the device is explicitly passed through from Windows and the correct kernel driver is loaded. If you hit this problem, see [WSL_WEBCAM_SETUP.md](WSL_WEBCAM_SETUP.md) for the full passthrough setup, including the two issues encountered while building this project (missing /dev/video* devices, and device permissions that reset on every WSL restart) and how they were resolved.

## 4. Installation <a name="installation"></a>

### Clone the repository

```bash
git clone <repository-url>
cd facial-recognition-system
```

###  Create the environment from `environment.yml`
The recommended way to install the project is with Conda using the provided `environment.yml` file. This creates an environment with the required Python, TensorFlow, CUDA, cuDNN, OpenCV, Matplotlib, and Jupyter versions.

```bash
conda env create -f environment.yml
conda activate facial-recognition
```

Manual installation see [MANUAL_INSTALLATION.md](MANUAL_INSTALLATION.md)

### Register the Jupyter kernel

```bash
python -m ipykernel install --user \
  --name facial-recognition \
  --display-name "Python 3.7 - Facial Recognition"
```

### Run the project

```bash
conda activate facial-recognition
```

### Start Jupyter Notebook

```bash
jupyter notebook
```
Select the kernel: Python 3.7 - Facial Recognition

## 5. Acknowledgement <a name="acknowledgement"></a>

This implementation is adapted from the facial recognition tutorial by **Nicholas Renotte**, which demonstrates a Siamese neural network for facial verification using TensorFlow and OpenCV.

The original tutorial structure and core implementation ideas include:

- collecting anchor and positive images with OpenCV;
- using LFW images as negative examples;
- creating image pairs with TensorFlow datasets;
- building a shared embedding network;
- implementing a custom L1 distance layer;
- training a Siamese network;
- evaluating precision and recall;
- performing real-time verification.

My modifications include:

- adapting the environment for WSL2: WSL_WEBCAM_SETUP.md
- creating a reproducible Conda environment
- documenting Python, TensorFlow, CUDA, and cuDNN compatibility;
- adding environment verification (debugging cells within the notebook)
- improving notebook organization and explanations;

Known issues:
Some environments display a NUMA-support warning when TensorFlow initializes the GPU. This warning is harmless as long as `tf.config.list_physical_devices("GPU")` returns a GPU and training runs successfully.

## 6. References <a name="references"></a>

[1] Nicholas Renotte (2021): Build a Deep Facial Recognition App from Paper to Code Youtube Tutorial: https://www.youtube.com/watch?v=bK_k7eebGgc&list=PLgNJO2hghbmhHuhURAGbe6KWpiYZt0AMH <br>
[2] JUPYTER NOTEBOOKS OF NICHOLAS RENOTTE: https://github.com/nicknochnack/FaceRecognition/tree/main <br>
[3] DATASET: https://www.kaggle.com/datasets/atulanandjha/lfwpeople <br>
[4] Koch, Gregory, Richard Zemel, and Ruslan Salakhutdinov (2015): Siamese neural networks for one-shot image: https://www.cs.utoronto.ca/~rsalakhu/papers/oneshot1.pdf <br>