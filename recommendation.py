import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# loading the data from the csv file to apandas dataframe
df = pd.read_csv("movies.csv")

# selecting the relevant features for recommendation you can choose any columns we wants it should we relevent to your recommendation

selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)

# selecting the relevant features for recommendation

selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)

# replacing the null valuess with null string

for feature in selected_features:
  df[feature] = df[feature].fillna('')

  #combining all the 5 selected features

# combining all the 5 selected features into a single text feature
combined_features = df['genres'] + ' ' + df['keywords'] + ' ' + df['tagline'] + ' ' + df['cast'] + ' ' + df['director']

# keep the original variable name used in later cells
movies_data = df

# converting the text data to feature vectors(text data to numerical data)

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

# getting the similarity scores using cosine similarity

similarity = cosine_similarity(feature_vectors)

import difflib

def recommend(movie_name):

    list_of_all_titles = df['title'].tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if len(find_close_match) == 0:
        return ["Movie not found"]

    close_match = find_close_match[0]

    index_of_the_movie = df[df.title == close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    sorted_similar_movies = sorted(
        similarity_score,
        key=lambda x: x[1],
        reverse=True
    )

    movie_names = []

    i = 1

    for movie in sorted_similar_movies:
        index = movie[0]

        title_from_index = df[df.index == index]['title'].values[0]

        if i < 30:
            movie_names.append(title_from_index)
            i += 1

    return movie_namesgit