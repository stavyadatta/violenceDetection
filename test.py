import numpy as np
import tensorflow as tf
import os
tf.compat.v1.disable_eager_execution()
# from keras.preprocessing.image import image
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.xception import Xception #preprocess_input -  when not using resnet 18
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.models import Sequential,Model,load_model
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D,GlobalAveragePooling2D
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
from imutils import paths
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import SGD, Adam
import cv2
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model
import pickle
from random import randint, shuffle
from classification_models import Classifiers