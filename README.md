# 🎬 Movie Recommender System
# 📌 Overview
This project is a content-based movie recommendation system built using Python, scikit-learn, and Streamlit. The system suggests movies based on their textual similarity using TF-IDF vectorization and cosine similarity. The application provides an intuitive web interface where users can search for a movie and receive personalized recommendations along with movie posters fetched from The Movie Database (TMDb) API.

# 🚀 Features
✅ Movie Recommendation: Get top 5 similar movies based on content similarity.
✅ Trending Movies Section: Displays posters of popular movies.
✅ Interactive UI: Built using Streamlit for a seamless user experience.
✅ Movie Poster Fetching: Uses TMDb API to retrieve movie posters.
✅ Efficient Search & Suggestions: Utilizes sklearn’s CountVectorizer for feature extraction.
✅ Pickle-Based Storage: Saves processed data for faster loading.

# 📂 Dataset & Model
The dataset is preprocessed by selecting relevant movie attributes (id, title, overview, genre).
Tags are created by combining overview and genre columns for similarity computation.
TF-IDF vectorization is applied to convert text data into numerical features.
Cosine similarity is used to compute similarity between movies.
The final model and processed dataset are saved as pickle files (movies_list.pkl, similarity.pkl) for efficient loading.

# 🛠️ Tech Stack
Python (Pandas, scikit-learn, requests, pickle)
Streamlit (Web framework)
The Movie Database (TMDb) API (Fetching movie posters)

# 🎥 Usage
Select a movie from the dropdown list.
Click the "Show Recommendations" button.
View the top 5 recommended movies with their posters.

# 📸 Demo
![Screenshot (114)](https://github.com/user-attachments/assets/0262546f-3344-4182-84f9-60a65ae4cd72)
