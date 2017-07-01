from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
#koristimo porterov stremmer za pronalazenja korena reci radi bolje klasifikacije
from porter2stemmer import  Porter2Stemmer
import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np
import time

import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import datetime
stemmer = LancasterStemmer()

tf.logging.set_verbosity(tf.logging.INFO)

COLUMNS = ["color","director_name","num_critic_for_reviews","duration","director_facebook_likes","actor_3_facebook_likes",
           "actor_2_name","actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users",
           "cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords","movie_imdb_link",
           "num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes",
           "imdb_score","aspect_ratio","movie_facebook_likes","people","category"]
FEATURES = ["genres", "plot_keywords", "movie_title", "actor_1_name", "actor_2_name", "actor_3_name", "director_name", "imdb_score"]
LABEL = "category"

TRAINING_SET = "TrainingSet/training.csv"
TEST_SET = "TestSet/test.csv"
json_training_data = []  # json lista

def GetRecommendations(file):

    porterStremmer = Porter2Stemmer()
    stemmer = LancasterStemmer()
    #ret1 = stemmer.stem("functionality")
    #ret2 = stemmer.stem("functions")
    #print(ret1)
    #print(ret2)

    #ret = porterStremmer.stem("functionality")
    #print(ret)
    #ret = porterStremmer.stem("function")
    #print(ret)

    tset = pd.read_csv(file, skipinitialspace=True, skiprows=1, names=COLUMNS)

    print(tset.shape)
    print(type(tset))
    words_set = tset.ix[:,['genres', 'plot_keywords', 'movie_title','people','imdb_score','category']]

    #print(words_set)

    training_list_items = []

    df = pd.DataFrame(columns=('all_words', 'class'))

    #prolazimo kroz trening set i pokupimo sve reci koje karakterisu film i ubacimo kao polje u json-u plus imdb rand i klasa

    i=0
    for index, row in words_set.iterrows():
        jedan_red_string = ""

        # m = row['movie_title'].split(' ')
        # for k in range(len(m)):
        #     s = m[k]
        #     jedan_red_string += stemmer.stem(s.lower())
        #     jedan_red_string += " "


        n = row['people'].split('|')
        for k in range(len(n)):
            s = n[k]
            jedan_red_string += stemmer.stem(s.lower())
            jedan_red_string += " "


        # rowrow = row['plot_keywords'].split('|')
        # for j in range(len(rowrow)):
        #     p = rowrow[j].split(' ')
        #     for k in range(len(p)):
        #         s = p[k]
        #         jedan_red_string += stemmer.stem(s.lower())
        #         jedan_red_string += " "

        g = row['genres'].split("|")
        for k in range(len(g)):
            s = g[k]
            jedan_red_string += s.lower()
            jedan_red_string += " "
        training_list_items.append(jedan_red_string)
        #print(jedan_red_string)

        json_training_data.append({"mwords":jedan_red_string,"class":row['category']})

        df.loc[i] = [jedan_red_string, row['category']]
        i += 1

    #print(df)


    #print(json_training_data)
    #print({"mwords":jedan_red_string,"imdb_score":row['imdb_score'], "class":row['category']})
    return df

def GetClassification(training_model=False):
    #nltk.download()

    words = []      #sve reci iz svih instanci
    classes = []    #sve klase koje postoje
    documents = []  #lista koja sadrzi bag od words za svaku instancu
    ignore_words = ['?']
    # loop through each sentence in our training data
    for pattern in json_training_data:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern['mwords'])
        # add to our words list
        words.extend(w)
        # add to documents in our corpus
        documents.append((w, pattern['class']))
        #print((w, pattern['class']))
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
        output_row[classes.index(doc[1])] = 1
        output.append(output_row)

    print("# words", len(words))
    print("# classes", len(classes))

    # i = 0
    # w = documents[i][0]
    # print ([stemmer.stem(word.lower()) for word in w])
    # print (training[i])
    # print (output[i])

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
        print(len(x))
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
            print("DEBUG_N: 1")
            print(layer_0.shape)
            layer_1 = sigmoid(np.dot(layer_0, synapse_0))
            print(synapse_0.shape)
            print(layer_1.shape)

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
        print("DEBUG_N 2")
        print(len(synapse_0.tolist()))
        synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),
                   'datetime': now.strftime("%Y-%m-%d %H:%M"),
                   'words': words,
                   'classes': classes
                   }
        print("DEBUG_N: 3")
        print(len(synapse['synapse0']))
        synapse_file = "synapses.json"

        with open(synapse_file, 'w') as outfile:
            json.dump(synapse, outfile, indent=4, sort_keys=True)
        print("saved synapses to:", synapse_file)


    if(training_model):
        X = np.array(training)
        y = np.array(output)

        print("podaci X i Y")
        print(X.shape)
        print(y.shape)
        start_time = time.time()
        print(start_time)

        #epochs vratiti na 100 000
        train(X, y, hidden_neurons=1, alpha=0.1, epochs=100000, dropout=False, dropout_percent=0.2)

        elapsed_time = time.time() - start_time
        print("processing time:", elapsed_time, "seconds")

    # probability threshold
    ERROR_THRESHOLD = 0.01
    # load our calculated synapse values
    synapse_file = 'synapses.json'
    with open(synapse_file) as data_file:
        synapse = json.load(data_file)
        synapse_0 = np.asarray(synapse['synapse0'])
        print("podaci u synapsi")
        print(len(synapse_0))
        print(synapse_0.shape)
        synapse_1 = np.asarray(synapse['synapse1'])
        print(len(synapse_1))
        print(synapse_1.shape)

    def classify(sentence, show_details=True):
        results = think(sentence, show_details)

        results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_results = [[classes[r[0]], r[1]] for r in results]
        print("%s \n classification: %s" % (sentence, return_results))
        return return_results


    x = classify("sylvester_stallone burgess_meredith carl_weathers john_g._avilds mal train drama sport")
    print(x)

def main():
    trening_skup = GetRecommendations(TRAINING_SET)
    test_skup = GetRecommendations(TEST_SET)

    trening_skup.to_csv("TrainingSet/reformated_training.csv", index=False)
    test_skup.to_csv("TestSet/reformated_test.csv", index=False)

    print("%s sentences in training data" % len(json_training_data))

    #kreiranje modela koji ce biti sacuvan u fajlu synapses.json
    GetClassification()




main()

