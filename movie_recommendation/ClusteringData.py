import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer

def readCsv(file_name):
    with open('RawDataSet/movies_formated.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader:
            print(row['director_name'], "\t\t", row['movie_title'])
            i += 1
            if (i > 10):
                break

def main():
    print("\n")
    raw_data = pd.read_csv("RawDataSet/movies_formated.csv")

    # prolazimo kroz sve atribute u csv fajlu i uzimamo samo one sa navedenim nazivima jer su nam korisni
    data_use = raw_data.ix[:,
               ['genres', 'plot_keywords', 'movie_title', 'actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name',
                'imdb_score']]
    data_use['movie_title'] = [i.replace("\xa0", "") for i in list(data_use['movie_title'])]

    print(data_use.shape)
    clean_data = data_use.dropna(axis=0)
    print(clean_data.shape)
    clean_data = clean_data.drop_duplicates(['movie_title'])
    clean_data = clean_data.reset_index(drop=True)
    print(clean_data.shape)

    people_list = []
    for i in range(clean_data.shape[0]):
        name1 = clean_data.ix[i, 'actor_1_name'].replace(" ", "_")
        name2 = clean_data.ix[i, 'actor_2_name'].replace(" ", "_")
        name3 = clean_data.ix[i, 'actor_3_name'].replace(" ", "_")
        name4 = clean_data.ix[i, 'director_name'].replace(" ", "_")
        people_list.append("|".join([name1, name2, name3, name4]))
    clean_data['people'] = people_list
    # print(clean_data)


    def token(text):
        return (text.split("|"))


    cv_kw = CountVectorizer(max_features=100, tokenizer=token)
    keywords = cv_kw.fit_transform(clean_data["plot_keywords"])

    keywords_list = ["kw_" + i for i in cv_kw.get_feature_names()]

    cv_ge = CountVectorizer(tokenizer=token)
    genres = cv_ge.fit_transform(clean_data["genres"])
    genres_list = ["genres_" + i for i in cv_ge.get_feature_names()]

    cv_pp = CountVectorizer(max_features=100, tokenizer=token)
    people = cv_pp.fit_transform(clean_data["people"])
    people_list = ["pp_" + i for i in cv_pp.get_feature_names()]

    cluster_data = np.hstack([keywords.todense(), genres.todense(), people.todense() * 2])
    criterion_list = keywords_list + genres_list + people_list

    from sklearn.cluster import KMeans

    mod = KMeans(n_clusters=50)
    category = mod.fit_predict(cluster_data)
    clean_data['category'] = category

    file_name = "ClusteredData/izlaz.csv"

    clean_data = clean_data.drop('people', 1)
    clean_data.to_csv(file_name, sep=',', index=False)
    print("Upisano u fajl izlaz.csv")

if __name__ == "__main__":
    main()
