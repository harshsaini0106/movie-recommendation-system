import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

print("Creating similarity matrix...")

# load movie dataset
movies = pickle.load(open('movie_list.pkl','rb'))

# use tags column
vectors = movies['tags']

# convert text to numeric vectors
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(vectors).toarray()

# calculate similarity
similarity = cosine_similarity(vectors)

# save similarity matrix
pickle.dump(similarity, open('similarity.pkl','wb'))

print("similarity.pkl created successfully!")