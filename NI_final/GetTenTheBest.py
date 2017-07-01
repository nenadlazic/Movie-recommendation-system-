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
from operator import itemgetter, attrgetter
import json


#Ova funkcija sluzi da u fajl current_recommendation.json upise 10 preporuka koje treba prikazati korisniku.
#kao argumente prima brojeve klastera kojima pripadaju filmovi koje je korisnik ocenio kao najbolje
def GetTheBest(cn1 = 1,cn2 = 2,cn3 = 3,cn4 = 4,cn5 = 5,cn6 = 6,cn7 = 7,cn8 = 8,cn9 = 9,cn10 = 10, num_ratings=4):
    file_name = "ClusteredData/clustered_data.csv"
    data = pd.read_csv(file_name)
    #print(data)

    #U listi recommendation ce se nalaziti 10 preporuka koje cemo prikazati korisniku, kao argument funkcije dobijama
    #10 oznaka klastera uredjenih tako da je prvi najbolje ocenje(sortirani u opadajucem)
    #po defaultu uzimamo iz prvog klastera 4, iz drugog 3 iz treceg 2 iz cetvrtog 1 ali posto teoretski moze da se desi da je prvi i drugi klaster
    # duzine 1 mi necemo imati dovoljno filmova pa cemo uzimati iz ostalih klastera vise situacija odabira 4:3:2:1 je samo u slucaju da imamo vise sa dobrim ocenama
    #i pod uslovom da u tim klasterima ima vise od 4 odn 3 odn 2 odnosno 1 filma

    lcn1 = []
    lcn2 = []
    lcn3 = []
    lcn4 = []
    lcn5 = []
    lcn6 = []
    lcn7 = []
    lcn8 = []
    lcn9 = []
    lcn10 = []
    for i in range(data.shape[0]):
        title = data.ix[i, 'movie_title']
        imdb = float(data.ix[i, 'imdb_score'])
        cat = int(data.ix[i, 'category'])
        #print(title, imdb, int(cat))
        if(cat == cn1):
            lcn1.append((title, imdb, cat))
        elif(cat == cn2):
            lcn2.append((title, imdb, cat))
        elif(cat == cn3):
            lcn3.append((title, imdb, cat))
        elif(cat == cn4):
            lcn4.append((title, imdb, cat))
        elif(cat == cn5):
            lcn5.append((title, imdb, cat))
        elif(cat == cn6):
            lcn6.append((title, imdb, cat))
        elif(cat == cn7):
            lcn7.append((title, imdb, cat))
        elif(cat == cn8):
            lcn8.append((title, imdb, cat))
        elif(cat == cn9):
            lcn9.append((title, imdb, cat))
        elif(cat == cn10):
            lcn10.append((title, imdb, cat))

    #svaku listu sortiramo rastuce po IMDB rangu
    lcn1 =sorted(lcn1, key=itemgetter(1), reverse=True)
    lcn2 =sorted(lcn2, key=itemgetter(1), reverse=True)
    lcn3 =sorted(lcn3, key=itemgetter(1), reverse=True)
    lcn4 =sorted(lcn4, key=itemgetter(1), reverse=True)
    lcn5 =sorted(lcn5, key=itemgetter(1), reverse=True)
    lcn6 =sorted(lcn6, key=itemgetter(1), reverse=True)
    lcn7 =sorted(lcn7, key=itemgetter(1), reverse=True)
    lcn8 =sorted(lcn8, key=itemgetter(1), reverse=True)
    lcn9 =sorted(lcn9, key=itemgetter(1), reverse=True)
    lcn10 =sorted(lcn10, key=itemgetter(1), reverse=True)

    # print(lcn1)
    # print(lcn2)
    # print(lcn3)
    # print(lcn4)
    # print(lcn5)
    # print(lcn6)
    # print(lcn7)
    # print(lcn8)
    # print(lcn9)
    # print(lcn10)
    counter_the_best = 0
    recommendation = []

    flg1 = True
    flg2 = False
    flg3 = False
    flg4 = False
    flg5 = False
    flg6 = False
    flg7 = False
    flg8 = False
    flg9 = False
    flg10 = False

    while(counter_the_best < 10):
        if(flg1):
            len_l1 = len(lcn1)
            if(len_l1 == 0):
                flg1 = False
                flg2 = True
            else:
                len_l1 = min(4, len_l1)
                for k in range(len_l1):
                    recommendation.append(lcn1[k][0])
                counter_the_best += k + 1
                flg1 = False
                flg2 =True
        elif(flg2):
            len_l2 = len(lcn2)
            if(len_l2 == 0):
                flg2 = False
                flg3 = True
            else:
                k = 0
                len_l2 = min(3, len_l1)
                for k in range(len_l2):
                    recommendation.append(lcn2[k][0])
                counter_the_best += k + 1
                flg2 = False
                flg3 =True
        elif (flg3):
            len_l3 = len(lcn3)
            if(len_l3 == 0):
                flg3 = False
                flg4 = True
            else:
                k = 0
                len_l3 = min(2, len_l3)
                for k in range(len_l3):
                    recommendation.append(lcn3[k][0])
                counter_the_best += k + 1
                flg3 = False
                flg4 = True
        elif (flg4):
            len_l4 = len(lcn4)
            if(len_l4 == 0):
                flg4 = False
                flg5 = True
            else:
                k = 0
                if(counter_the_best<7):
                    len_l4 = min(2,len_l4)
                else:
                    len_l4 = 1
                for k in range(len_l4):
                    recommendation.append(lcn4[k][0])
                counter_the_best += k + 1
                flg4 = False
                flg5 = True
        elif (flg5):
            if(len(lcn5) == 0):
                flg5 = False
                flg6 = True
            else:
                recommendation.append(lcn5[0][0])
                counter_the_best += 1
                flg5 = False
                flg6 = True
        elif (flg6):
            if(len(lcn6) == 0):
                flg6 = False
                flg7 = True
            else:
                recommendation.append(lcn6[0][0])
                counter_the_best += 1
                flg6 = False
                flg7 = True
        elif (flg7):
            if(len(lcn7) == 0):
                flg7 = False
                flg8 = True
            else:
                recommendation.append(lcn7[0][0])
                counter_the_best += 1
                flg7 = False
                flg8 = True
        elif (flg8):
            if(len(lcn8) == 0):
                flg8 = False
                flg9 = True
            else:
                recommendation.append(lcn8[0][0])
                counter_the_best += 1
                flg8 = False
                flg9 = True
        elif (flg9):
            if(len(lcn9) == 0):
                flg9 = False
                flg10 = True
            else:
                recommendation.append(lcn9[0][0])
                counter_the_best += 1
                flg9 = False
                flg10 = True
        elif (flg10):
            if(len(lcn10) == 0):
                flg10 = False
            else:
                recommendation.append(lcn10[0][0])
                counter_the_best += 1
                flg10 = False

    #print("Preporuke:")
    #print(recommendation)
    #print(len(recommendation))

    recommendation_full_info = []
    raw_data = pd.read_csv("RawData/movies_formated.csv")
    for i in range(raw_data.shape[0]):
        row_title = raw_data.ix[i, 'movie_title']
        for j in recommendation:
            if(j == row_title):
                #recommendation_full_info.append(i)
                a1 = raw_data.ix[i, 'actor_1_name']
                a2 = raw_data.ix[i, 'actor_2_name']
                a3 = raw_data.ix[i, 'actor_3_name']
                a4 = raw_data.ix[i, 'director_name']
                a5 = raw_data.ix[i, 'genres']
                a6 = raw_data.ix[i, 'movie_title']
                a7 = raw_data.ix[i, 'plot_keywords']
                a8 = raw_data.ix[i, 'movie_imdb_link']

                instance = (a1,a2,a3,a4,a5,a6,a7,a8)
                recommendation_full_info.append(instance)



    #print("#########################################################################")
    # with open('current_recommendation.json', 'w') as outfile:
    #     json.dump(recommendation_full_info, outfile)

    with open('RecommendedMovie/current_recommendation2.json', 'w') as fp:
        fp.write('<table border="1" id="tbl"><tr> <th>Actor1</th><th>Actor2</th> <th>Actor3</th><th>Director</th><th>Genres</th><th>Title</th><th>HashTags</th><th>Trailer</th></tr>')
        fp.write('\n'.join('<tr><th> %s </th><th> %s </th><th> %s </th><th> %s </th><th> %s </th><th> %s </th><th> %s </th><th> <a href="%s">watch trailer</a> </th></tr> ' % x for x in recommendation_full_info))
        fp.write('</table>')

def main():
    print("Entered function main in module GetTenTheBest")
if __name__ == '__main__':
    print("Function GetTenTheBest finished")
    #GetAllClusters()
    #GetTheBest(22,45,68,47,25,3,4,61,55,24)