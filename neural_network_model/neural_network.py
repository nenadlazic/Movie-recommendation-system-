from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib
import urllib.request
import base64

import numpy as np
import tensorflow as tf

# Data sets
IRIS_TRAINING = "iris_training.csv"
IRIS_TRAINING_URL = "http://download.tensorflow.org/data/iris_training.csv"

IRIS_TEST = "iris_test.csv"
IRIS_TEST_URL = "http://download.tensorflow.org/data/iris_test.csv"

def main():
  print("executed")
  # If the training and test sets aren't stored locally, download them.
  if not os.path.exists(IRIS_TRAINING):
    raw = urllib.request.urlopen(IRIS_TRAINING_URL).read()
    print(raw)
    with open(IRIS_TRAINING, "wb") as f:
      f.write(raw)
      print(raw)

  if not os.path.exists(IRIS_TEST):
    raw = urllib.request.urlopen(IRIS_TEST_URL).read()
    print(raw)
    with open(IRIS_TEST, "wb") as f:
      f.write(raw)
      print(raw)



#Load dataset in python data structure
# Load datasets.
  training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=IRIS_TRAINING,
    target_dtype=np.int,
    features_dtype=np.float32)
  print(training_set)
  test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
    filename=IRIS_TEST,
    target_dtype=np.int,
    features_dtype=np.float32)


  

if __name__ == "__main__":
    main()
