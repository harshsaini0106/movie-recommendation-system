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
    
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    
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
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])