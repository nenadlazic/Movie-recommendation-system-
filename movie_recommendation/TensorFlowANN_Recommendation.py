from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import tempfile

from six.moves import urllib

import pandas as pd
import tensorflow as tf



COLUMNS = ["color","director_name","num_critic_for_reviews","duration","director_facebook_likes","actor_3_facebook_likes",
           "actor_2_name","actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users",
           "cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords","movie_imdb_link",
           "num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes",
           "imdb_score","aspect_ratio","movie_facebook_likes"]
LABEL_COLUMN = "category"
CATEGORICAL_COLUMNS = ["color"]
CONTINUOUS_COLUMNS = ["duration"]




def build_estimator(model_dir, model_type):
  """Build an estimator."""
  # Sparse base columns.
  m_color = tf.contrib.layers.sparse_column_with_keys(column_name="color", keys=["Color", "Black and White"])

  # Continuous base columns.
  m_duration = tf.contrib.layers.real_valued_column("duration")

  # Transformations.
  m_duration_buckets = tf.contrib.layers.bucketized_column(m_duration,
                                                    boundaries=[
                                                        30, 50, 65, 80, 95, 110,
                                                        130, 155, 180, 200,500
                                                    ])

  # Wide columns and deep columns.
  wide_columns = [m_color]
  deep_columns = [
      tf.contrib.layers.embedding_column(m_color, dimension=8),
      m_duration,
  ]

  if model_type == "wide":
    m = tf.contrib.learn.LinearClassifier(model_dir=model_dir,
                                          feature_columns=wide_columns)
  elif model_type == "deep":
    m = tf.contrib.learn.DNNClassifier(model_dir=model_dir,
                                       feature_columns=deep_columns,
                                       hidden_units=[10, 5])
  else:
    m = tf.contrib.learn.DNNLinearCombinedClassifier(
        model_dir=model_dir,
        linear_feature_columns=wide_columns,
        dnn_feature_columns=deep_columns,
        dnn_hidden_units=[10, 5],
        fix_global_step_increment_bug=True)
  return m


def input_fn(df):
  """Input builder function."""
  # Creates a dictionary mapping from each continuous feature column name (k) to
  # the values of that column stored in a constant Tensor.
  continuous_cols = {k: tf.constant(df[k].values) for k in CONTINUOUS_COLUMNS}
  # Creates a dictionary mapping from each categorical feature column name (k)
  # to the values of that column stored in a tf.SparseTensor.
  categorical_cols = {
      k: tf.SparseTensor(
          indices=[[i, 0] for i in range(df[k].size)],
          values=df[k].values,
          dense_shape=[df[k].size, 1])
      for k in CATEGORICAL_COLUMNS}
  # Merges the two dictionaries into one.
  feature_cols = dict(continuous_cols)
  feature_cols.update(categorical_cols)
  # Converts the label column into a constant Tensor.
  label = tf.constant(df[LABEL_COLUMN].values)
  # Returns the feature columns and the label.
  return feature_cols, label


def train_and_eval(model_dir, model_type, train_steps, train_data, test_data):
  """Train and evaluate the model."""
  train_file_name = "ClusteredData/training.csv"
  test_file_name = "ClusteredData/test.csv"

  df_train = pd.read_csv(
      tf.gfile.Open(train_file_name),
      names=COLUMNS,
      skipinitialspace=True,
      engine="python")
  df_test = pd.read_csv(
      tf.gfile.Open(test_file_name),
      names=COLUMNS,
      skipinitialspace=True,
      skiprows=1,
      engine="python")

  print(df_test)

  # remove NaN elements
  df_train = df_train.dropna(how='any', axis=0)
  df_test = df_test.dropna(how='any', axis=0)

  df_train[LABEL_COLUMN] = (
      df_train["income_bracket"].apply(lambda x: ">50K" in x)).astype(int)
  df_test[LABEL_COLUMN] = (
      df_test["income_bracket"].apply(lambda x: ">50K" in x)).astype(int)

  model_dir = tempfile.mkdtemp() if not model_dir else model_dir
  print("model directory = %s" % model_dir)

  m = build_estimator(model_dir, model_type)
  m.fit(input_fn=lambda: input_fn(df_train), steps=train_steps)
  results = m.evaluate(input_fn=lambda: input_fn(df_test), steps=1)
  for key in sorted(results):
    print("%s: %s" % (key, results[key]))


FLAGS = None


def main(_):
  train_and_eval(FLAGS.model_dir, FLAGS.model_type, FLAGS.train_steps,
                 FLAGS.train_data, FLAGS.test_data)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.register("type", "bool", lambda v: v.lower() == "true")
  parser.add_argument(
      "--model_dir",
      type=str,
      default="",
      help="Base directory for output models."
  )
  parser.add_argument(
      "--model_type",
      type=str,
      default="wide_n_deep",
      help="Valid model types: {'wide', 'deep', 'wide_n_deep'}."
  )
  parser.add_argument(
      "--train_steps",
      type=int,
      default=200,
      help="Number of training steps."
  )
  parser.add_argument(
      "--train_data",
      type=str,
      default="",
      help="Path to the training data."
  )
  parser.add_argument(
      "--test_data",
      type=str,
      default="",
      help="Path to the test data."
  )
  FLAGS, unparsed = parser.parse_known_args()
  tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)