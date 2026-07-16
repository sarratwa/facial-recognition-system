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

Unlike a conventional multi-class classifier, the model does not directly predict a person's identity. Instead, it receives two images and learns whether the images represent the same person.

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

## 3. Data <a name="data"></a>

The project uses three image categories:

- **Anchor images:** reference images of the target person.
- **Positive images:** additional images of the same person.
- **Negative images:** images of other people.

The negative examples are taken from the [Labeled Faces in the Wild (LFW)](https://www.kaggle.com/datasets/atulanandjha/lfwpeople) dataset.

> [!IMPORTANT]
> The notebook resizes images to `100 × 100` pixels and scales pixel values to the range `[0, 1]`.

todo: document clearly how an evaluator can provide their own images

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
> [!NOTE]
> ### Manual installation
> Use this method only when the environment file cannot be used.
> #### Create the Conda environment
> ```bash
> conda create -n facial-recognition python=3.7 -y
> conda activate facial-recognition
> ```
> #### Install CUDA dependencies for GPU use
> ```bash
> conda install -c conda-forge cudatoolkit=11.0 cudnn=8.0 -y
> ```
> #### Install Python dependencies
> ```bash
> python -m pip install -r requirements.txt
> ```

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

- adapting the environment for WSL2;
- creating a reproducible Conda environment;
- documenting Python, TensorFlow, CUDA, and cuDNN compatibility;
- adding environment verification;
- improving notebook organization and explanations;
- TODO: list all further code, evaluation, robustness, and visualization changes.

## 6. References <a name="references"></a>

```text
[1] Nicholas Renotte (2021): Build a Deep Facial Recognition App from Paper to Code Youtube Tutorial: https://www.youtube.com/watch?v=bK_k7eebGgc&list=PLgNJO2hghbmhHuhURAGbe6KWpiYZt0AMH 
[2] JUPYTER NOTEBOOKS OF NICHOLAS RENOTTE: https://github.com/nicknochnack/FaceRecognition/tree/main
[3] DATASET: https://www.kaggle.com/datasets/atulanandjha/lfwpeople
[4] Koch, Gregory, Richard Zemel, and Ruslan Salakhutdinov (2015): Siamese neural networks for one-shot image: https://www.cs.utoronto.ca/~rsalakhu/papers/oneshot1.pdf
```
 