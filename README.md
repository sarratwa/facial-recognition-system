# Deep Facial Recognition System

The focus of the project was understanding how deep learning techniques can be applied to biometric authentication systems and facial verification tasks.

## Project Pipeline

1. Install Dependencies around Tensorflow

!pip install tensorflow==2.4.1 tensorflow-gpu==2.4.1 opencv-python matplotlib
-> explain why it works on ubuntu / wsl windows
-> another point is tensorflow-gpu failed python_version>"3.7" This error originates from a subprocess, and is likely not a problem with pip. error: metadata-generation-failed

pip install tensorflow-gpu==2.4.1
ERROR: Could not find a version that satisfies the requirement tensorflow-gpu==2.4.1 (from versions: 2.12.0)
ERROR: No matching distribution found for tensorflow-gpu==2.4.1

Software requirements
Python 3.9–3.12

https://www.tensorflow.org/install/pip

-> new one is python3 -m pip install 'tensorflow[and-cuda]'

2. Importing Tensorflow Functional API
3. Setting up to Limit your GPU growth 
4. Create Data Folders and Structure

## Installation

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
