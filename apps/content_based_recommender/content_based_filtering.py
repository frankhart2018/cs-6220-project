import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    layout="wide",
    page_title="Content Based Filtering",
)

st.title("Select the algorithm to use for content based filtering:")

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div class="row" style="margin-left: 10px;">
        <div class="card" style="width: 18rem; margin-right: 10px;">
          <div class="card-body">
            <h5 class="card-title">TfIdf</h5>
            <p class="card-text" style='text-align: justify; text-justify: inter-word;'>Using TfIdf for content based filtering.</p>
            <br>
            <a href="https://share.streamlit.io/frankhart2018/cs-6220-project/siddhartha/apps/content_based_recommender/tfidf_recommender.py" class="btn btn-primary" target="_blank" style="position: absolute; left: 0;  right: 0; bottom: 0">Check it out</a>
          </div>
        </div>
        <div class="card" style="width: 18rem; margin-right: 10px;">
          <div class="card-body">
            <h5 class="card-title">NN</h5>
            <p class="card-text" style='text-align: justify; text-justify: inter-word;'>Using NN for content based filtering.</p>
            <br>
            <a href="https://share.streamlit.io/frankhart2018/cs-6220-project/siddhartha/apps/content_based_recommender/nn_recommender.py" class="btn btn-primary" target="_blank" style="position: absolute; left: 0;  right: 0; bottom: 0">Check it out</a>
          </div>
        </div>
    </div>
    """,
    height=600,
)