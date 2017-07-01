from sklearn.externals import joblib
import pickle
from porter2stemmer import  Porter2Stemmer
import re
import time
import warnings

import GetTenTheBest as gttb

porterStremmer = Porter2Stemmer()

#pronalazi za instance koje je user ocenio kao najbolje i koje su upisane u fajl UserRatings/instances.txt
#tu listu vrati u glavni metod i odatle se koristi da se iz tih klastera odabere odgovarajuci broj preporuka
def GetCluster(loc_actor1_name, loc_actor2_name, loc_actor3_name, loc_director_name, loc_movie_title, loc_keywords, loc_genres):
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)

    #Ucitavamo kreirani model iz fajla
    #loaded_model = joblib.load(filename)
    #result = loaded_model.score(x_test, y_test)

    with open("criterion_list.txt", "rb") as fp:
        list_criterion = pickle.load(fp)
        #print(list_criterion)
        #print(len(list_criterion))

    #root
    #MYSECRET
    #kao argument funkcije potrebno je zadati ime 3 glumca iz filma, ime rezisera, naziv filma, zanrove kojima pripada i nazi filma
    actor1_name = loc_actor1_name
    actor2_name = loc_actor2_name
    actor3_name = loc_actor3_name
    director_name = loc_director_name
    movie_title = loc_movie_title
    keywords = loc_keywords
    genres = loc_genres

    actor1_name = actor1_name.replace(" ", "_")
    actor1_name = ("pp_"+actor1_name).lower()

    actor2_name = actor2_name.replace(" ", "_")
    actor2_name = ("pp_"+actor2_name).lower()

    actor3_name = actor3_name.replace(" ", "_")
    actor3_name = ("pp_"+actor3_name).lower()

    director_name = director_name.replace(" ", "_")
    director_name = ("pp_"+director_name).lower()

    #print(actor1_name)
    #print(actor2_name)
    #print(actor3_name)
    #print(director_name)

    list_people = []
    list_people.append(actor1_name)
    list_people.append(actor2_name)
    list_people.append(actor3_name)
    list_people.append(director_name)


    one_row = keywords.split("|")
    #print(one_row)

    # prolazi se kroz svaki deo te splitovane liste i dodatno se splituje sa spaceom
    changed_row = ""
    br1 = 0
    list_kw = []
    for i in one_row:



        k = i.split(" ")
        item_wrd = ""
        br = 0
        for j in k:
            #print(j)
            porswrd = porterStremmer.stem(j)
            #print(porswrd)
            if br > 0:
                item_wrd += "_"
            item_wrd += porswrd
            br += 1
        #print(item_wrd)
        item_wrd = "kw_"+item_wrd
        list_kw.append(item_wrd)
        if br1 > 0:
            changed_row += "|"
        changed_row += item_wrd
        br1 += 1
    #print(changed_row)
    #print(list_kw)

    l_genres = []
    lg = genres.split("|")
    for i in lg:
        k = "genres_"+i.lower()
        l_genres.append(k)
    #print(l_genres)

    list_all_data = []

    for i in list_people:
        list_all_data.append(i)
    for i in list_kw:
        list_all_data.append(i)
    for i in l_genres:
        list_all_data.append(i)

    sample = [0] * (len(list_criterion))
    s = []
    #print(sample)
    #print(len(sample))
    #print(len(list_criterion))

    k = 0
    for i in list_criterion:
        flag = False
        for j in list_all_data:
            if i == j:
                flag = True
        if flag:
            s.append(1)
            #print("nadjena neka rec")
        else:
            s.append(0)

        k += 1

    #print(len(s))

    #print(list_all_data)

    #Ucitavamo kreirani model iz fajla
    filename = 'Model/finalized_model.sav'
    loaded_model = joblib.load(filename)
    ls = []
    ls.append(s)
    result = loaded_model.predict(ls)
    #print("Zadata instanca pripada klasteru:")
    #print(result)
    return int(result)

#Color,Andrew Adamson,258.0,150.0,80.0,201.0,Pierfrancesco Favino,22000.0,141614023.0,Action|Adventure|Family|Fantasy,Peter Dinklage,The Chronicles of Narnia: Prince Caspian ,149922,22697,Dami??n Alc??zar,4.0,narnia,http://www.imdb.com/title/tt0499448/?ref_=fn_tt_tt_1,438.0,English,USA,PG,225000000.0,2008.0,216.0,6.6,2.35,0,Peter_Dinklage|Pierfrancesco_Favino|Dami??n_Alc??zar|Andrew_Adamson,20
#def GetCluster(loc_actor1_name, loc_actor2_name, loc_actor3_name, loc_director_name, loc_movie_title, loc_keywords, loc_genres):



def GetAllClusters():
    filename = "UserRatings/instances.txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()
    #print(lines)

    pattern = re.compile(r'(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*)', re.M)

    list_cluster = []

    for i in lines:
        #print(i)

        match_object = pattern.match(i)
        if(match_object):
            actor1 = match_object.group(1)
            actor2 = match_object.group(2)
            actor3 = match_object.group(3)
            director = match_object.group(4)
            title = match_object.group(5)
            keywords = match_object.group(6)
            genres = match_object.group(7)
            #print(actor1, actor2, actor3, director, title, keywords, genres)

            cls = GetCluster(actor1, actor2, actor3, director, title, keywords, genres)
            list_cluster.append(cls)
    #test
    # GetCluster("Andrew Adamson", "Pierfrancesco Favino", "Peter Dinklage", "Dami??n Alc??zar", "The Chronicles of Narnia: Prince Caspian","narnia","Action|Adventure|Family|Fantasy")

    #print(list_cluster)
    return list_cluster

def main():
    print("#################### Get all clusters started ##############################")
    start_time = time.time()
    l = GetAllClusters()
    end_time = time.time()
    print("execution time: %s seconds" % (end_time - start_time))
    print("#################### Get all clusters finished ##############################")

    print("#################### Get Ten The BEst started ##############################")
    start_time = time.time()
    gttb.GetTheBest(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8],l[9])
    end_time = time.time()
    print("execution time: %s seconds" % (end_time - start_time))
    print("#################### Get Ten The BEst finished ##############################")


if __name__ == '__main__':
    main()
