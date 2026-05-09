import streamlit as st
import pandas as pd
import os
from recommend import get_recommendations, build_model

st.set_page_config(page_title="Movie Recommender", page_icon="🎬")
st.title("🎬 Movie Recommendation System")
st.markdown("Select a movie you like and get 10 similar recommendations!")

if not os.path.exists('similarity.pkl'):
    with st.spinner('Building recommendation model... please wait'):
        build_model()

df = pd.read_csv('data/movies.csv')
movie_list = df['title'].tolist()

movie = st.selectbox("Choose a movie", movie_list)

if st.button("Get Recommendations"):
    results = get_recommendations(movie)
    st.subheader("You might also like:")
    for i, r in enumerate(results, 1):
        st.markdown(f"**{i}.** {r}")
