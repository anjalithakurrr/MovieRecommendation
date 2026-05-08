import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

def build_model():
    df = pd.read_csv('data/movies.csv')
    df['genres'] = df['genres'].fillna('')

    tfidf = TfidfVectorizer(stop_words='english')
    matrix = tfidf.fit_transform(df['genres'])
    sim = cosine_similarity(matrix)

    with open('similarity.pkl', 'wb') as f:
        pickle.dump((df, sim), f)
    print("✅ Model built and saved!")

def get_recommendations(title, n=10):
    with open('similarity.pkl', 'rb') as f:
        df, sim = pickle.load(f)

    matches = df[df['title'] == title]
    if matches.empty:
        return ["Movie not found in dataset."]

    idx = matches.index[0]
    scores = sorted(enumerate(sim[idx]), key=lambda x: x[1], reverse=True)[1:n+1]
    indices = [i[0] for i in scores]
    return df['title'].iloc[indices].tolist()

if __name__ == '__main__':
    build_model()