import os

if not os.path.exists("similarity.pkl"):
    import create_similarity

import streamlit as st
import pickle
import requests

# Load data
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


# Fetch movie poster
def fetch_poster(movie_id):

    api_key = "282dfcf7bf624fd28b95dc075297fb5f"

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

    response = requests.get(url)

    if response.status_code != 200:
        return "https://via.placeholder.com/500x750?text=No+Image"

    data = response.json()

    poster_path = data.get('poster_path')

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"


# Recommendation function
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x:x[1]
    )[1:16]

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


if st.button("Recommend"):

    names, posters = recommend(selected_movie)

    for i in range(0, len(names), 5):

        cols = st.columns(5)

        for j in range(5):

            if i+j < len(names):

                with cols[j]:

                    st.text(names[i+j])

                    st.image(posters[i+j])