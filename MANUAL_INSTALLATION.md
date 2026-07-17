

### Manual installation
Use this method only when the environment file cannot be used.
#### Create the Conda environment
```bash
conda create -n facial-recognition python=3.7 -y
conda activate facial-recognition
```
#### Install CUDA dependencies for GPU use
```bash
conda install -c conda-forge cudatoolkit=11.0 cudnn=8.0 -y
```
#### Install Python dependencies
```bash
python -m pip install -r requirements.txt
