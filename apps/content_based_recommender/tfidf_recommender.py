import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import pandas as pd
import pickle


def recommend_movies_based_on_plot(movie_name, mapping, similarity_matrix):
    if movie_name == "--Select a movie--":
        return ""

    movie_index = mapping[movie_name]
    similarity_score = list(enumerate(similarity_matrix[movie_index]))
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    similarity_score = similarity_score[1:6]
    movie_indices = [i[0] for i in similarity_score]

    ret_str = "The movies that you might also like are: <br><br><ul>"
    for title in df['Title'].iloc[movie_indices]:
        ret_str += "<li>" + title + "</li>"
    ret_str += "</ul>"

    return ret_str


st.set_page_config(
    page_title="Content Based Filtering",
)

st.title("Content Based Filtering (TfIdf)")

show_info = st.checkbox("Show details")

if show_info:
    st.markdown("""
**How are recommending similar movies?**

The first step we performed was to take the movies plot and pass it through an algorithm called Tf-Idf (Term Frequency-
Inverse Document Frequency) which is a technique to convert the movie plots into a sparse vector representation.
Once, this is computed, we can use this to create a similarity matrix with an algorithm called 
linear kernel (available in scikit-learn). This matrix is then used to compute the similarity between 
movies.
    """)
else:
    st.write("")

df = pd.read_csv("movies_filled_cleaned_processed.csv")

similarity_matrix = np.load("data/similarity_matrix_tfidf.npy")

with open("data/df_mapping_tfidf", "rb") as f:
    df_mapping = pickle.load(f)

movie_titles_tup = tuple(["--Select a movie--"] + df['Title'].tolist())

movie_name = st.selectbox(
    "Select a movie",
    movie_titles_tup
)

components.html(recommend_movies_based_on_plot(
    movie_name=movie_name,
    similarity_matrix=similarity_matrix,
    mapping=df_mapping)
)