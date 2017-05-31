import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

TRAINING_SET = "ClusteredData/training.csv"
TEST_SET = "ClusteredData/test.csv"

dataset_file = "ClusteredData/izlaz.csv"
COLUMNS = ["genres", "plot_keywords", "movie_title", "actor_1_name", "actor_2_name", "actor_3_name", "director_name","imdb_score", "category"]


def divide_dataset(test_percentage = 20):
    dataset_frame = pd.read_csv(dataset_file, skipinitialspace=True, skiprows=1, names=COLUMNS)
    print(dataset_frame.head(5))
    print(dataset_frame.__len__())



    train, test = train_test_split(dataset_frame, test_size=(test_percentage*1.0)/100)
    print(type(train))
    print(type(test))

    print(train.head(5))
    print("duzina ",len(train))
    print(test.head(5))
    print("duzina ",len(test))


    train.to_csv(TRAINING_SET, sep=',', index=False)
    print("Upisano u fajl training.csv")
    test.to_csv(TEST_SET, sep=',', index=False)
    print("Upisano u fajl test.csv")

divide_dataset()