import streamlit as st
import pickle
import requests


# Function to fetch movie poster with error handling
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/500x750.png?text=No+Image"


# Load movie data
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Streamlit App Title
st.title("🎬 Movie Recommender System")

# Default Poster Carousel (Popular Movies)
st.subheader("🔥 Trending Movies")
popular_movie_ids = [1632, 299536, 17455, 2830, 429422, 9722, 13972, 240, 155, 598, 914, 255709, 572154]
popular_posters = [fetch_poster(movie_id) for movie_id in popular_movie_ids]

# Display posters in a grid (first 5 trending movies)
cols = st.columns(5)
for col, poster in zip(cols, popular_posters[:5]):
    with col:
        st.image(poster, width=120)

# Movie selection dropdown
selectvalue = st.selectbox("🎥 Select a movie:", movies_list)


# Function to get recommendations
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])

    recommended_movies = []
    recommended_posters = []

    for i in distances[1:6]:  # Get top 5 similar movies
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# Show recommendations when button is clicked
if st.button("🔍 Show Recommendations"):
    st.subheader("📌 Recommended Movies")

    movie_names, movie_posters = recommend(selectvalue)
    cols = st.columns(5)  # 5 columns for 5 recommended movies

    for col, name, poster in zip(cols, movie_names, movie_posters):
        with col:
            st.image(poster, width=140)
            st.text(name)
