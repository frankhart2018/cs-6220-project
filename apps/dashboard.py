import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    layout="wide",
    page_title="Team Orion (CS-6220)",
)

st.title("Team Orion Project - Highest Grossing Movies Dataset")

show_info = st.checkbox("Show details")

if show_info:
    st.markdown("""
**Dataset used**

For our project we used the [Top 1000 Highest Grossing Movies Dataset](https://www.kaggle.com/datasets/sanjeetsinghnaik/top-1000-highest-grossing-movies) 
from Kaggle. This dataset consists details like movie title, plot, release date, world, domestic, and international gross.

**Tasks**

The cards displayed below are the various tasks that we performed on the dataset.
    """)
else:
    st.write("")

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div class="row" style="margin-left: 10px;">
        <div class="card" style="width: 18rem; margin-right: 10px;">
          <div class="card-body">
            <h5 class="card-title">Movie similarity plots</h5>
            <p class="card-text" style='text-align: justify; text-justify: inter-word; word-break: break-all'>Using techniques like sentence embeddings, t-SNE, and PCA we have created a visualization that shows similar movies in a 2-D space.</p>
            <br>
            <a href="https://share.streamlit.io/frankhart2018/cs-6220-project/siddhartha/apps/movie_desc_embeddings/movies_embeddings.py" class="btn btn-primary" target="_blank" style="position: absolute; left: 0;  right: 0; bottom: 0">Check it out</a>
          </div>
        </div>
        <div class="card" style="width: 18rem; margin-right: 10px;">
          <div class="card-body">
            <h5 class="card-title">Content-based recommender</h5>
            <p class="card-text" style='text-align: justify; text-justify: inter-word; word-break: break-all'>Using content-based filtering technique, we present simple recommender systems that recommend you movies based on titles that you have already watched.</p>
            <br>
            <a href="https://share.streamlit.io/frankhart2018/cs-6220-project/siddhartha/apps/content_based_recommender/content_based_filtering.py" class="btn btn-primary" target="_blank" style="position: absolute; left: 0;  right: 0; bottom: 0">Check it out</a>
          </div>
        </div>
        <div class="card" style="width: 18rem; margin-right: 10px;">
          <div class="card-body">
            <h5 class="card-title">Genre popularity</h5>
            <p class="card-text" style='text-align: justify; text-justify: inter-word; word-break: break-all'>Which genres are most popular, and which genres match together.</p>
            <br>
            <a href="https://share.streamlit.io/frankhart2018/cs-6220-project/siddhartha/apps/genre_popularity/genre_popularity_curves.py" class="btn btn-primary" target="_blank" style="position: absolute; left: 0;  right: 0; bottom: 0">Check it out</a>
          </div>
        </div>
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">Distributor Sales</h5>
            <p class="card-text" style='text-align: justify; text-justify: initial; word-break: break-all'>Which distributors are most popular at domestic, international, and world level.</p>
            <br>
            <a href="https://share.streamlit.io/frankhart2018/cs-6220-project/siddhartha/apps/distributor/distributor_sales.py" class="btn btn-primary" target="_blank" style="position: absolute; left: 0;  right: 0; bottom: 0">Check it out</a>
          </div>
        </div>
    </div>
    
    <div class="row" style="margin-left: 10px; margin-top: 10px;">
        <div class="card" style="width: 18rem; margin-right: 10px;">
          <div class="card-body">
            <h5 class="card-title">Topic modelling</h5>
            <p class="card-text" style='text-align: justify; text-justify: inter-word; word-break: break-all'>Using techniques like sentence embeddings, t-SNE, and PCA we have created a visualization that shows similar movies in a 2-D space.</p>
            <br>
            <a href="https://share.streamlit.io/frankhart2018/cs-6220-project/siddhartha/apps/topic_modelling/topic_modelling.py" class="btn btn-primary" target="_blank" style="position: absolute; left: 0;  right: 0; bottom: 0">Check it out</a>
          </div>
        </div>
        <div class="card" style="width: 18rem; margin-right: 10px;">
          <div class="card-body">
            <h5 class="card-title">Genre over years</h5>
            <p class="card-text" style='text-align: justify; text-justify: inter-word; word-break: break-all'>The trend in popular genres over the years from 1940s-2020s. How popular is your favourite genre?</p>
            <br>
            <a href="https://share.streamlit.io/frankhart2018/cs-6220-project/siddhartha/apps/genre_over_years/genre_over_years.py" class="btn btn-primary" target="_blank" style="position: absolute; left: 0;  right: 0; bottom: 0">Check it out</a>
          </div>
        </div>
        <div class="card" style="width: 18rem; margin-right: 10px;">
          <div class="card-body">
            <h5 class="card-title">Genre prediction</h5>
            <p class="card-text" style='text-align: justify; text-justify: inter-word; word-break: break-all'>Predicting the genre of a movie, given its plot. Select your favourite movie from among the listed titles and get its genre.</p>
            <br>
            <a href="https://share.streamlit.io/frankhart2018/cs-6220-project/siddhartha/apps/genre_prediction/genre_prediction.py" class="btn btn-primary" target="_blank" style="position: absolute; left: 0;  right: 0; bottom: 0">Check it out</a>
          </div>
        </div>
    </div>
    """,
    height=600,
)

st.markdown("""
# Code

If you want to access the code for this project, you can find it on 
[GitHub CS-6220 Project](https://github.com/frankhart2018/cs-6220-project). This contains the code base
for data preprocessing, modelling and the streamlit applications. 
""")