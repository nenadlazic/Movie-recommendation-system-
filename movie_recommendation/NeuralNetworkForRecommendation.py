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
    words_set = tset.ix[:,['genres', 'plot_keywords', 'movie_title','people','imdb_score','category']]

   # print(words_set)

    training_list_items = []


    #prolazimo kroz trening set i pokupimo sve reci koje karakterisu film i ubacimo kao polje u json-u plus imdb rand i klasa
    json_training_data = [] #json lista
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

        g = row['genres'].split("|")
        for k in range(len(g)):
            s = g[k]
            jedan_red_string += porterStremmer.stem(s.lower())
            jedan_red_string += " "
        training_list_items.append(jedan_red_string)
        #print(jedan_red_string)

        json_training_data.append({"mwords":jedan_red_string,"imdb_score":row['imdb_score'], "class":row['category']})
        #print({"mwords":jedan_red_string,"imdb_score":row['imdb_score'], "class":row['category']})





    print("%s sentences in training data" % len(json_training_data))

    #nltk.download()

    words = []
    classes = []
    documents = []
    ignore_words = ['?']
    # loop through each sentence in our training data
    for pattern in json_training_data:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern['mwords'])
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, pattern['imdb_score'], pattern['class']))
        # add to our classes list
        if pattern['class'] not in classes:
            classes.append(pattern['class'])

    # stem and lower each word and remove duplicates
    words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
    words = list(set(words))

    # remove duplicates
    classes = list(set(classes))

    print(len(documents), "documents")
    print(len(classes), "classes", classes)
    print(len(words), "unique stemmed words", words)

    # create our training data
    training = []
    output = []
    # create an empty array for our output
    output_empty = [0] * len(classes)

    # training set, bag of words for each sentence
    for doc in documents:
        # initialize our bag of words
        bag = []
        # list of tokenized words for the pattern
        pattern_words = doc[0]
        # stem each word
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
        # create our bag of words array
        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)

        training.append(bag)
        # output is a '0' for each tag and '1' for current tag
        output_row = list(output_empty)
        output_row[classes.index(doc[2])] = 1
        output.append(output_row)

    print("# words", len(words))
    print("# classes", len(classes))

    i = 0
    w = documents[i][0]
    print ([stemmer.stem(word.lower()) for word in w])
    print (training[i])
    print (output[i])

    import numpy as np
    import time

    # compute sigmoid nonlinearity
    def sigmoid(x):
        output = 1 / (1 + np.exp(-x))
        return output

    # convert output of sigmoid function to its derivative
    def sigmoid_output_to_derivative(output):
        return output * (1 - output)

    def clean_up_sentence(sentence):
        # tokenize the pattern
        sentence_words = nltk.word_tokenize(sentence)
        # stem each word
        sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words

    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
    def bow(sentence, words, show_details=False):
        # tokenize the pattern
        sentence_words = clean_up_sentence(sentence)
        # bag of words
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % w)

        return (np.array(bag))

    def think(sentence, show_details=False):
        x = bow(sentence.lower(), words, show_details)
        if show_details:
            print("sentence:", sentence, "\n bow:", x)
        # input layer is our bag of words
        l0 = x
        # matrix multiplication of input and hidden layer
        l1 = sigmoid(np.dot(l0, synapse_0))
        # output layer
        l2 = sigmoid(np.dot(l1, synapse_1))
        return l2

    # ANN and Gradient Descent code from https://iamtrask.github.io//2015/07/27/python-network-part2/
    def train(X, y, hidden_neurons=10, alpha=1, epochs=50000, dropout=False, dropout_percent=0.5):

        print("Training with %s neurons, alpha:%s, dropout:%s %s" % (
        hidden_neurons, str(alpha), dropout, dropout_percent if dropout else ''))
        print("Input matrix: %sx%s    Output matrix: %sx%s" % (len(X), len(X[0]), 1, len(classes)))
        np.random.seed(1)

        last_mean_error = 1
        # randomly initialize our weights with mean 0
        synapse_0 = 2 * np.random.random((len(X[0]), hidden_neurons)) - 1
        synapse_1 = 2 * np.random.random((hidden_neurons, len(classes))) - 1

        prev_synapse_0_weight_update = np.zeros_like(synapse_0)
        prev_synapse_1_weight_update = np.zeros_like(synapse_1)

        synapse_0_direction_count = np.zeros_like(synapse_0)
        synapse_1_direction_count = np.zeros_like(synapse_1)

        for j in iter(range(epochs + 1)):

            # Feed forward through layers 0, 1, and 2
            layer_0 = X
            layer_1 = sigmoid(np.dot(layer_0, synapse_0))

            if (dropout):
                layer_1 *= np.random.binomial([np.ones((len(X), hidden_neurons))], 1 - dropout_percent)[0] * (
                1.0 / (1 - dropout_percent))

            layer_2 = sigmoid(np.dot(layer_1, synapse_1))

            # how much did we miss the target value?
            layer_2_error = y - layer_2

            if (j % 10000) == 0 and j > 5000:
                # if this 10k iteration's error is greater than the last iteration, break out
                if np.mean(np.abs(layer_2_error)) < last_mean_error:
                    print("delta after " + str(j) + " iterations:" + str(np.mean(np.abs(layer_2_error))))
                    last_mean_error = np.mean(np.abs(layer_2_error))
                else:
                    print("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error)
                    break

            # in what direction is the target value?
            # were we really sure? if so, don't change too much.
            layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

            # how much did each l1 value contribute to the l2 error (according to the weights)?
            layer_1_error = layer_2_delta.dot(synapse_1.T)

            # in what direction is the target l1?
            # were we really sure? if so, don't change too much.
            layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)

            synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
            synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))

            if (j > 0):
                synapse_0_direction_count += np.abs(
                    ((synapse_0_weight_update > 0) + 0) - ((prev_synapse_0_weight_update > 0) + 0))
                synapse_1_direction_count += np.abs(
                    ((synapse_1_weight_update > 0) + 0) - ((prev_synapse_1_weight_update > 0) + 0))

            synapse_1 += alpha * synapse_1_weight_update
            synapse_0 += alpha * synapse_0_weight_update

            prev_synapse_0_weight_update = synapse_0_weight_update
            prev_synapse_1_weight_update = synapse_1_weight_update

        now = datetime.datetime.now()

        # persist synapses
        synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),
                   'datetime': now.strftime("%Y-%m-%d %H:%M"),
                   'words': words,
                   'classes': classes
                   }
        synapse_file = "synapses.json"

        with open(synapse_file, 'w') as outfile:
            json.dump(synapse, outfile, indent=4, sort_keys=True)
        print("saved synapses to:", synapse_file)

    #X = np.array(training[:20])
    #y = np.array(output[:20])

    #start_time = time.time()

    #train(X, y, hidden_neurons=20, alpha=0.1, epochs=100000, dropout=False, dropout_percent=0.2)

    #elapsed_time = time.time() - start_time
    #print("processing time:", elapsed_time, "seconds")


    



GetRecommendations()