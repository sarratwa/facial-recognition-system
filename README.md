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
