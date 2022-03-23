import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    layout="wide",
    page_title="Team Orion (CS-6220)",
)

st.title("Team Orion Project - Highest Grossing Movies Dataset")

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div class="row" style="margin-left: 10px;">
        <div class="card" style="width: 18rem; margin-right: 10px;">
          <div class="card-body">
            <h5 class="card-title">Movie similarity plots</h5>
            <p class="card-text" style='text-align: justify; text-justify: inter-word;'>Using techniques like sentence embeddings, t-SNE, and PCA we have created a visualization that shows similar movies in a 2-D space</p>
            <a href="https://share.streamlit.io/frankhart2018/cs-6220-project/siddhartha/apps/movie_desc_embeddings/movies_embeddings.py" class="btn btn-primary" target="_blank">Check it out</a>
          </div>
        </div>
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">Content based recommender</h5>
            <p class="card-text" style='text-align: justify; text-justify: inter-word;'>Using content-based filtering technique, we present simple recommender systems that recommend you movies based on titles that you have already watched</p>
            <a href="https://share.streamlit.io/frankhart2018/cs-6220-project/siddhartha/apps/content_based_recommender/tfidf_recommender.py" class="btn btn-primary" target="_blank">Check it out</a>
          </div>
        </div>
    </div>
    """,
    height=600,
)