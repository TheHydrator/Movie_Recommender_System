import streamlit as st
import pickle
import pandas as pd
import requests


# Function to fetch the poster and Google search URL of the movie
def fetch_poster_and_url(movie_id, movie_title):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=3f63b8ac769f4634a544f33033e7a7fa&language=en-US'.format(movie_id))
    data = response.json()
    poster_url = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    google_search_url = f"https://www.google.com/search?q={movie_title.replace(' ', '+')}"
    return poster_url, google_search_url


# Function to recommend movies
def recommend(movie, movies_data):
    movie_index = movies_data[movies_data['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_ = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_urls = []
    for i in movies_list_:
        movie_id = movies_data.iloc[i[0]].movie_id
        movie_title = movies_data.iloc[i[0]].title
        poster_url, google_search_url = fetch_poster_and_url(movie_id, movie_title)
        recommended_movies.append(movie_title)
        recommended_movies_posters.append(poster_url)
        recommended_movies_urls.append(google_search_url)
    return recommended_movies, recommended_movies_posters, recommended_movies_urls


# Load the model and the movie list
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Which movie do you like best?',
    movies['title'].values)

if st.button('Recommend'):
    names, posters, urls = recommend(selected_movie_name, movies_data=movies)
    cols = st.columns(5) # 5 columns to display the recommendations

    for i, col in enumerate(cols):
        col.markdown(f"[{names[i]}]({urls[i]})")
        col.image(posters[i])

