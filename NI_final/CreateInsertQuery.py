import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib
from tempfile import TemporaryFile
import pickle
from porter2stemmer import  Porter2Stemmer


def CreateQuery():
    raw_data = pd.read_csv("RawData/movies_formated.csv")
    s = "INSERT INTO `movies`(`movie_id`, `actor1`, `actor2`, `actor3`, `director`, `keywords`, `genres`, `title`) VALUES "
    flag = False
    for iw in range(raw_data.shape[0]):
        if(flag):
            s += ","
        a1 = str(raw_data.ix[iw, 'actor_1_name']).replace("'","")
        a2 = str(raw_data.ix[iw, 'actor_2_name']).replace("'","")
        a3 = str(raw_data.ix[iw, 'actor_3_name']).replace("'","")
        a4 = str(raw_data.ix[iw, 'director_name']).replace("'","")
        a5 = str(raw_data.ix[iw, 'plot_keywords']).replace("'","")
        a6 = str(raw_data.ix[iw, 'genres']).replace("'","")
        a7 = str(raw_data.ix[iw, 'movie_title']).replace("'","")
        s1 = "('"+str(a1)+"','"+str(a2)+"','"+str(a3)+"','"+str(a4)+"','"+str(a5)+"','"+str(a6)+"','"+str(a7)+"')"
        s += s1
        flag = True
        s1 = ""

    s += ";"

    print(s)

CreateQuery()