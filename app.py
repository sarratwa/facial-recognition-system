import matplotlib
import cv2
import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))
print(tf.__version__)
print("TensorFlow:", tf.__version__)
# print("GPUs:", tf.config.list_physical_devices("GPU"))

# tensorflow only works on Linux -> switch to wsl

