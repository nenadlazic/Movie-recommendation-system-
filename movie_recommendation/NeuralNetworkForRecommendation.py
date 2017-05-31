from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import itertools

import pandas as pd
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

COLUMNS = ["genres", "plot_keywords", "movie_title", "actor_1_name", "actor_2_name", "actor_3_name", "director_name", "imdb_score", "category"]
FEATURES = ["genres", "plot_keywords", "movie_title", "actor_1_name", "actor_2_name", "actor_3_name", "director_name", "imdb_score"]
LABEL = "category"

TRAINING_SET = "ClusteredData/training.csv"
TEST_SET = "ClusteredData/test.csv"

def GetRecommendations():



GetRecommendations()