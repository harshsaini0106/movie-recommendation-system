# 🎬 Movie Recommendation System

A Machine Learning based Movie Recommendation System that suggests similar movies based on content similarity.

This project uses **Natural Language Processing (NLP)** and **Cosine Similarity** to recommend movies similar to the one selected by the user.

---

## 🚀 Live Demo

Click here to try the app:

👉 **[Movie Recommendation System](https://movie-recommendation-system-kqlaynvzqgwijappnrgt8yt.streamlit.app/)**

# 🚀 Features

✔ Recommend similar movies
✔ Content-based filtering
✔ NLP text processing
✔ Cosine similarity algorithm
✔ Interactive web interface
✔ Movie poster display using TMDB API

---

# 🧠 Machine Learning Concepts Used

* Natural Language Processing (NLP)
* Text Vectorization (CountVectorizer)
* Cosine Similarity
* Feature Engineering
* Recommendation Systems

---

# 🛠 Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* TMDB API
* Pickle

---

# 📂 Project Structure

movie-recommender-system
│
├── app.py
├── movies.pkl
├── create_similarity.py
├── requirements.txt
├── .gitignore
└── README.md

---

# ⚙️ Installation

Clone the repository

```
git clone https://github.com/yourusername/movie-recommender-system.git
```

Go to the project folder

```
cd movie-recommender-system
```

Install required libraries

```
pip install -r requirements.txt
```

---

# ▶️ Run the Project

Generate similarity matrix

```
python create_similarity.py
```

Run the Streamlit app

```
streamlit run app.py
```

---

# ⚠️ Note

The file **similarity.pkl** is not included in the repository because it exceeds GitHub's file size limit.

Run the following command to generate it:

```
python create_similarity.py
```

---

# 🎥 Dataset

Dataset used: **TMDB 5000 Movie Dataset**

---

# 🌐 Future Improvements

* Add collaborative filtering
* Add deep learning recommendation model
* Add user login system
* Add movie rating prediction
* Deploy on cloud (Streamlit / AWS)

---

# 👨‍💻 Author

Harsh Saini
Aspiring Machine Learning Engineer

---
