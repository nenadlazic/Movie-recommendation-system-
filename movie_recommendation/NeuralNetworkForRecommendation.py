from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
#koristimo porterov stremmer za pronalazenja korena reci radi bolje klasifikacije
from porter2stemmer import  Porter2Stemmer
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
stemmer = LancasterStemmer()

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

    print(tset.shape)
    print(type(tset))
    words_set = tset.ix[:,['genres', 'plot_keywords', 'movie_title','people']]

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
    print(corpus)



    #test set
    test_set = pd.read_csv(TEST_SET, skipinitialspace=True, skiprows=1, names=COLUMNS)
    words_set_test = test_set.ix[:,['plot_keywords', 'movie_title','people']]

    x = words_set_test.ix[:,['people']]

    test_list_items = []


    for index, row in words_set_test.iterrows():
        jedan_red_string_test = ""

        m = row['movie_title'].split(' ')
        for k in range(len(m)):
            s = m[k]
            jedan_red_string_test += porterStremmer.stem(s.lower())
            jedan_red_string_test += " "


        n = row['people'].split('|')
        for k in range(len(n)):
            s = n[k]
            jedan_red_string_test += porterStremmer.stem(s.lower())
            jedan_red_string_test += " "


        rowrow = row['plot_keywords'].split('|')
        for j in range(len(rowrow)):
            p = rowrow[j].split(' ')
            for k in range(len(p)):
                s = p[k]
                jedan_red_string_test += porterStremmer.stem(s.lower())
                jedan_red_string_test += " "
        test_list_items.append(jedan_red_string_test)

    corpus_test = test_list_items
    print(corpus_test)

    #racunamo tf-idf meru za trening set
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    print(tfidf_matrix.shape)
    print(type(tfidf_matrix))
    np.set_printoptions(threshold=np.nan)
    print(tfidf_matrix)

    coo = tfidf_matrix.tocoo(copy=False)
    nenad = pd.DataFrame({'index': coo.row, 'col': coo.col, 'data': coo.data}
                 )[['index', 'col', 'data']].sort_values(['index', 'col']
                                                         ).reset_index(drop=True)

    print(nenad)

    from sklearn.neural_network import MLPClassifier


GetRecommendations()