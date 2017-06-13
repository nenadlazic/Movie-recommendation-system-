from sklearn.externals import joblib
import pickle
from porter2stemmer import  Porter2Stemmer

porterStremmer = Porter2Stemmer()

def GetCluster():
    #Ucitavamo kreirani model iz fajla
    #loaded_model = joblib.load(filename)
    #result = loaded_model.score(x_test, y_test)

    with open("criterion_list.txt", "rb") as fp:
        list_criterion = pickle.load(fp)
        print(list_criterion)
        print(len(list_criterion))

    #kao argument funkcije potrebno je zadati ime 3 glumca iz filma, ime rezisera, naziv filma, zanrove kojima pripada i nazi filma
    actor1_name = "neko ime"
    actor2_name = "neko ime"
    actor3_name = "neko ime"
    director_name = "neko ime"
    movie_title = "neko ime"
    keywords = "neko ime"

    actor1_name = actor1_name.replace(" ", "_")
    actor1_name = ("pp_"+actor1_name).lower()

    actor2_name = actor2_name.replace(" ", "_")
    actor2_name = ("pp_"+actor2_name).lower()

    actor3_name = actor3_name.replace(" ", "_")
    actor3_name = ("pp_"+actor3_name).lower()

    director_name = director_name.replace(" ", "_")
    director_name = ("pp_"+director_name).lower()

    print(actor1_name)
    print(actor2_name)
    print(actor3_name)
    print(director_name)

    list_people = []
    list_people.append(actor1_name)
    list_people.append(actor2_name)
    list_people.append(actor3_name)
    list_people.append(director_name)

    keywords = "neka rec|neka druga|kraj"

    one_row = keywords.split("|")
    print(one_row)

    # prolazi se kroz svaki deo te splitovane liste i dodatno se splituje sa spaceom
    changed_row = ""
    br1 = 0
    list_kw = []
    for i in one_row:



        k = i.split(" ")
        item_wrd = ""
        br = 0
        for j in k:
            print(j)
            porswrd = porterStremmer.stem(j)
            print(porswrd)
            if br > 0:
                item_wrd += "_"
            item_wrd += porswrd
            br += 1
        print(item_wrd)
        item_wrd = "kw_"+item_wrd
        list_kw.append(item_wrd)
        if br1 > 0:
            changed_row += "|"
        changed_row += item_wrd
        br1 += 1
    print(changed_row)
    print(list_kw)

    #kreiramo listu zanrova
    genres = "action|comedy"
    l_genres = []
    lg = genres.split("|")
    for i in lg:
        k = "genres_"+i.lower()
        l_genres.append(k)
    print(l_genres)

    list_all_data = []

    for i in list_people:
        list_all_data.append(i)
    for i in list_kw:
        list_all_data.append(i)
    for i in l_genres:
        list_all_data.append(i)

    sample = [0] * (len(list_criterion))
    s = []
    print(sample)
    print(len(sample))
    print(len(list_criterion))

    k = 0
    for i in list_criterion:
        flag = False
        for j in list_all_data:
            if i == j:
                flag = True
        if flag:
            s.append(1)
            print("nadjena neka rec")
        else:
            s.append(0)

        k += 1

    print(len(s))

    #print(list_all_data)

    #Ucitavamo kreirani model iz fajla
    filename = 'Model/finalized_model.sav'
    loaded_model = joblib.load(filename)
    ls = []
    ls.append(s)
    result = loaded_model.predict(ls)
    print(result)

GetCluster()

