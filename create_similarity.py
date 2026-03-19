import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# load movies data
movies = pickle.load(open('movie_list.pkl','rb'))

# use the tags column
vectors = movies['tags']

# convert text to vectors
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(vectors).toarray()

# calculate similarity
similarity = cosine_similarity(vectors)

# save similarity matrix
pickle.dump(similarity, open('similarity.pkl','wb'))

print("similarity.pkl created successfully!")