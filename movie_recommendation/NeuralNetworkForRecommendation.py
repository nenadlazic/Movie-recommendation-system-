from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
#koristimo porterov stremmer za pronalazenja korena reci radi bolje klasifikacije
from porter2stemmer import  Porter2Stemmer
from sklearn.feature_extraction.text import CountVectorizer
import tensorflow as tf
import pandas as pd

tf.logging.set_verbosity(tf.logging.INFO)

COLUMNS = ["genres", "plot_keywords", "movie_title", "actor_1_name", "actor_2_name", "actor_3_name", "director_name", "imdb_score", "people","category"]
FEATURES = ["genres", "plot_keywords", "movie_title", "actor_1_name", "actor_2_name", "actor_3_name", "director_name", "imdb_score"]
LABEL = "category"

TRAINING_SET = "ClusteredData/training.csv"
TEST_SET = "ClusteredData/test.csv"

def GetRecommendations():

    porterStremmer = Porter2Stemmer()
    #test
    #ret = x.stem("factionally")
    #print(ret)

    tset = pd.read_csv(TRAINING_SET, skipinitialspace=True, skiprows=1, names=COLUMNS)

    words_set = tset.ix[:,['plot_keywords', 'movie_title','people']]

    x = words_set.ix[:,['people']]

    training_list_items = []


    for index, row in words_set.iterrows():
        jedan_red_string = ""

        m = row['movie_title'].split(' ')
        for k in range(len(m)):
            s = m[k]
            jedan_red_string += porterStremmer.stem(s.lower())
            jedan_red_string += " "


        n = row['people'].split('|')
        for k in range(len(n)):
            s = n[k]
            jedan_red_string += porterStremmer.stem(s.lower())
            jedan_red_string += " "


        rowrow = row['plot_keywords'].split('|')
        for j in range(len(rowrow)):
            p = rowrow[j].split(' ')
            for k in range(len(p)):
                s = p[k]
                jedan_red_string += porterStremmer.stem(s.lower())
                jedan_red_string += " "
        training_list_items.append(jedan_red_string)

    corpus = training_list_items

    vectorizer = CountVectorizer()
    vectorizer.fit_transform(corpus)
    print(vectorizer.vocabulary_)





GetRecommendations()