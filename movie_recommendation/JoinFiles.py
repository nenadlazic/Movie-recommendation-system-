import pandas as pd


def join_data_frames():

    file1_name = "ClusteredData/izlaz.csv"
    file2_name = "RawDataSet/movie_formated.csv"

    COLUMNS1 = ["genres", "plot_keywords", "movie_title", "actor_1_name", "actor_2_name", "actor_3_name","director_name", "imdb_score", "people", "category"]
    COLUMNS2 = ["color","director_name","num_critic_for_reviews","duration","director_facebook_likes","actor_3_facebook_likes","actor_2_name","actor_1_facebook_likes","gross","genres","actor_1_name","movie_title","num_voted_users","cast_total_facebook_likes","actor_3_name","facenumber_in_poster","plot_keywords","movie_imdb_link","num_user_for_reviews","language","country","content_rating","budget","title_year","actor_2_facebook_likes","imdb_score","aspect_ratio","movie_facebook_likes"]

    first_frame = pd.read_csv(file1_name, skipinitialspace=True, skiprows=1, names=COLUMNS1)
    second_frame = pd.read_csv(file1_name, skipinitialspace=True, skiprows=1, names=COLUMNS2)

    result = first_frame.merge(second_frame, on='movie_title', how='left')

    print(result)
    result.head(5)


join_data_frames()