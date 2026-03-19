import os

if not os.path.exists("similarity.pkl"):
    import create_similarity
import streamlit as st
import pickle
import pandas as pd
import requests

# Load saved data
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Fetch movie poster from TMDB
def fetch_poster(movie_id):

    api_key = "282dfcf7bf624fd28b95dc075297fb5f"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    data = requests.get(url)
    data = data.json()

    poster_path = data['poster_path']

    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    return full_path


# Recommendation Function
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:16]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:

        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# Streamlit UI
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

# Button
if st.button("Recommend"):

    names, posters = recommend(selected_movie)

    for i in range(0, len(names), 5):
        cols = st.columns(5)

        for j in range(5):
            if i + j < len(names):
                with cols[j]:
                    st.text(names[i + j])
                    st.image(posters[i + j])