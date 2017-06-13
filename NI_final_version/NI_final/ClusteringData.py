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

def clustering_data():
    #ucitavamo csv fajl koji sadrzi podatke o filmovima sa 28 atributa
    raw_data = pd.read_csv("RawData/movies_formated.csv")

    porterStremmer = Porter2Stemmer()

    # prolazimo kroz sve atribute u csv fajlu i uzimamo samo one sa navedenim nazivima jer su nam korisni
    data_use = raw_data
    data_use['movie_title'] = [i.replace("\xa0", "") for i in list(data_use['movie_title'])]

    #izbacujemo instance sa nedostajucim vrednostima
    print("Ukupan broj ucitanih instanci i broj atributa")
    print(data_use.shape)
    print(type(data_use))
    print("Ukupan broj ucitanih instanci koji imaju poznate vrednosti za svaki atribut")
    clean_data = data_use.dropna(axis=0, how='any')
    print(clean_data.shape)
    print("Ukupan broj ucitanih instanci sa izbacenim duplikatima")
    clean_data = clean_data.drop_duplicates(['movie_title'])
    clean_data = clean_data.reset_index(drop=True)
    print(clean_data.shape)

    lkw = []
    for iw in range(clean_data.shape[0]):
        #lista splitovana sa | predstavlja jednu instancu
        one_row = clean_data.ix[iw, 'plot_keywords'].split("|")
        print(one_row)

        #prolazi se kroz svaki deo te splitovane liste i dodatno se splituje sa spaceom
        for i in one_row:

            br1 = 0
            changed_row = ""

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

            if br1 > 0:
                changed_row += "|"
            changed_row += item_wrd
        lkw.append(changed_row)
    clean_data['plot_keywords'] = lkw


    #prolazimo kroz dataframe i za svaku instancu uzimamo imena 3 glumca i direktora filma
    #U dataframu kolene su zapravo liste tako da ih na taj nacin mozemo tretirati
    people_list = []
    for i in range(clean_data.shape[0]):
        name1 = clean_data.ix[i, 'actor_1_name'].replace(" ", "_")
        name2 = clean_data.ix[i, 'actor_2_name'].replace(" ", "_")
        name3 = clean_data.ix[i, 'actor_3_name'].replace(" ", "_")
        name4 = clean_data.ix[i, 'director_name'].replace(" ", "_")
        people_list.append("|".join([name1, name2, name3, name4]))
    clean_data['people'] = people_list


    def token(text):
        return (text.split("|"))




    #CounterVectorizer se koristi za izracunavanje TF(term frequency) mere
    cv_kw = CountVectorizer(max_features=3000, tokenizer=token)
    #razdvajaju se reci delimiteron | i dodaju u countervectorizer(to je neki dictionary)
    keywords = cv_kw.fit_transform(clean_data["plot_keywords"])

    #Prolazi se kroz nazive kolona(atributa) i dodaje im se prefiks kw_
    keywords_list = ["kw_" + i.replace(" ","_") for i in cv_kw.get_feature_names()]
    #pravi se novi CounterVectorizer za zanr(posto jedan film moze pripadati vise zanrova
    cv_ge = CountVectorizer(tokenizer=token)
    genres = cv_ge.fit_transform(clean_data["genres"])
    genres_list = ["genres_" + i for i in cv_ge.get_feature_names()]

    cv_pp = CountVectorizer(max_features=3000, tokenizer=token)
    people = cv_pp.fit_transform(clean_data["people"])
    people_list = ["pp_" + i for i in cv_pp.get_feature_names()]

    cluster_data = np.hstack([keywords.todense(), genres.todense(), people.todense() * 2])
    criterion_list = keywords_list + genres_list + people_list
    print("Podaci o keywords listi: ")
    print(len(keywords_list))
    print(keywords_list)

    print("Podaci o genres listi: ")
    print(len(genres_list))
    print(genres_list)

    print("Podaci o people listi ")
    print(len(people_list))
    print(people_list)

    mod = KMeans(n_clusters=50)
    category = mod.fit_predict(cluster_data)
    clean_data['category'] = category

    file_name = "ClusteredData/clustered_data.csv"
    clean_data.to_csv(file_name, sep=',', index=False)
    print("Klasterovani podaci su upisani u fajl ClusteredData/clustered_data.csv")

    print("dimenzije cluster data")
    print(cluster_data.shape)
    #print(cluster_data[0])
    #ova funkcija vrati  cluster_data i category
    #onda se neuronska mreza istrenira na tome i onda treba samo za novu instancu izracunati kao sto je za ove gore racunato
    #ispreprocesirati ih i dati mrezi
    #klasifikacija

    print(type(cluster_data))

    #podelicemo podatke na test i trening skup
    x_train, x_test, y_train, y_test = train_test_split(cluster_data, category, test_size=0.20, random_state=0)

    print("podela na trening i test u odnosu:")
    print(type(x_train))
    print(len(x_train))
    print(len(x_test))

    print(type(cluster_data))
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(40,), random_state=1)
    clf.fit(x_train, y_train)
    #j = clf.predict([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
    #print(j)

    #score = clf.score(x_test, y_test)
    #print("accuracy: ",score)

    outfile_data = TemporaryFile(dir="PreprocessedData")
    outfile_class = TemporaryFile(dir="PreprocessedData")


    np.save(outfile_data, x_test)
    np.save(outfile_class, y_test)
    outfile_data.seek(0)
    outfile_class.seek(0)
    testovi_x = np.load(outfile_data)
    testovi_y = np.load(outfile_class)

    filename = 'Model/finalized_model.sav'
    joblib.dump(clf, filename)

    # load the model from disk
    loaded_model = joblib.load(filename)
    result = loaded_model.score(x_test, y_test)
    print("rezultat kod")
    print(result)

    print("rezultat fajl: ")
    res = loaded_model.score(testovi_x, testovi_y)
    print(res)

    print("criterion_list: ")
    print(criterion_list)
    with open("criterion_list.txt", "wb") as fp:
        pickle.dump(criterion_list, fp)



clustering_data()

#probati tretirati kao kategoricki atribut i iskoristiti porterov stemer