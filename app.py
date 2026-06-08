import os
<<<<<<< HEAD
import streamlit as st
import pickle
import requests

# If similarity file doesn't exist, create it
if not os.path.exists("similarity.pkl"):
    import create_similarity

# Page config
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS for dark theme & hover effect
st.markdown("""
<style>
/* Body background */
body {
    background-color: #0E1117;
}

/* Main title */
h1 {
    text-align: center;
    color: #FF4B4B;
}

/* Movie title under poster */
.movie-title{
    text-align:center;
    font-weight:bold;
    font-size:16px;
    color:white;
}

/* Hover effect on images */
img:hover {
    transform: scale(1.05);
    transition: 0.3s;
}
</style>
""", unsafe_allow_html=True)

# Load data
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# TMDB API key (replace with your own if needed)
API_KEY = "282dfcf7bf624fd28b95dc075297fb5f"

# Fetch movie poster from TMDB
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
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
    try:
        movie_index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error("Movie not found!")
        return [], []

    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:16]  # top 15 recommendations
=======

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
>>>>>>> 110d015999e5cc3744a5cbbefcf45ca8433fa3a5

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
<<<<<<< HEAD
        movie_id = movies.iloc[i[0]].movie_id
=======

        movie_id = movies.iloc[i[0]].movie_id

>>>>>>> 110d015999e5cc3744a5cbbefcf45ca8433fa3a5
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

<<<<<<< HEAD
# UI Title
st.markdown("<h1>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("### Find movies similar to your favourite ones 🍿")

# Movie selection dropdown
selected_movie = st.selectbox(
    "Search or select a movie",
    movies['title'].values
)

# Recommend button
if st.button("🎥 Show Recommendations"):

    with st.spinner("Finding similar movies..."):
        names, posters = recommend(selected_movie)

    if names and posters:
        for i in range(0, len(names), 5):
            cols = st.columns(5)
            for j in range(5):
                if i + j < len(names):
                    with cols[j]:
                        st.image(posters[i+j])
                        st.markdown(
                            f"<div class='movie-title'>{names[i+j]}</div>",
                            unsafe_allow_html=True
                        )
=======

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
>>>>>>> 110d015999e5cc3744a5cbbefcf45ca8433fa3a5
