import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def clustering_data():
    raw_data = pd.read_csv("RawDataSet/movies_formated.csv")

    # prolazimo kroz sve atribute u csv fajlu i uzimamo samo one sa navedenim nazivima jer su nam korisni
    data_use = raw_data
    data_use['movie_title'] = [i.replace("\xa0", "") for i in list(data_use['movie_title'])]

    print("Ukupan broj ucitanih instanci i broj atributa")
    print(data_use.shape)
    print(type(data_use))
    print("Ukupan broj ucitanih instanci koji imaju poznate vrednosti za svaki atribut")
    clean_data = data_use.dropna(axis=0)
    print(clean_data.shape)
    print("Ukupan broj ucitanih instanci sa izbacenim duplikatima")
    clean_data = clean_data.drop_duplicates(['movie_title'])
    clean_data = clean_data.reset_index(drop=True)
    print(clean_data.shape)

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
    cv_kw = CountVectorizer(max_features=100, tokenizer=token)
    #razdvajaju se reci delimiteron | i dodaju u countervectorizer(to je neki dictionary)
    keywords = cv_kw.fit_transform(clean_data["plot_keywords"])

    #Prolazi se kroz nazive kolona(atributa) i dodaje im se prefiks kw_
    keywords_list = ["kw_" + i for i in cv_kw.get_feature_names()]
    #pravi se novi CounterVectorizer za zanr(posto jedan film moze pripadati vise zanrova
    cv_ge = CountVectorizer(tokenizer=token)
    genres = cv_ge.fit_transform(clean_data["genres"])
    genres_list = ["genres_" + i for i in cv_ge.get_feature_names()]

    cv_pp = CountVectorizer(max_features=100, tokenizer=token)
    people = cv_pp.fit_transform(clean_data["people"])
    people_list = ["pp_" + i for i in cv_pp.get_feature_names()]

    cluster_data = np.hstack([keywords.todense(), genres.todense(), people.todense() * 2])
    criterion_list = keywords_list + genres_list + people_list


    mod = KMeans(n_clusters=50)
    category = mod.fit_predict(cluster_data)
    clean_data['category'] = category

    file_name = "ClusteredData/izlaz.csv"
    clean_data.to_csv(file_name, sep=',', index=False)
    print("Klasterovani podaci su upisani u fajl ClusteredData/izlaz.csv")

clustering_data()