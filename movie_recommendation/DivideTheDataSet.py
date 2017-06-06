import pandas as pd
from sklearn.model_selection import train_test_split

TRAINING_SET = "ClusteredData/training.csv"
TEST_SET = "ClusteredData/test.csv"

dataset_file = "ClusteredData/izlaz.csv"

COLUMNS = ["color","director_name","num_critic_for_reviews","duration","director_facebook_likes","actor_3_facebook_likes",
           "actor_2_name","actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users",
           "cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords","movie_imdb_link",
           "num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes",
           "imdb_score","aspect_ratio","movie_facebook_likes","category"]
#Svakim pokretanjem ove funkcije dobijamo drugacije podele instanci u trening setu i test setu
def divide_dataset(test_percentage = 30):
    dataset_frame = pd.read_csv(dataset_file, skipinitialspace=True, skiprows=1, names=COLUMNS)

    train, test = train_test_split(dataset_frame, test_size=(test_percentage*1.0)/100)

    print("Duzina trening skupa: ",len(train))
    print("Duzina test skupa",len(test))


    train.to_csv(TRAINING_SET, sep=',', index=False)
    print("Trening instance su upisane u fajl ClusteredData/training.csv")
    test.to_csv(TEST_SET, sep=',', index=False)
    print("Test instance su upisane u fajl ClusteredData/test.csv")

divide_dataset()