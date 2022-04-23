import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    layout="wide",
    page_title="Team Orion",
)

st.title("Team Orion - Members")

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div class="row" style="margin-left: 10px;">
        <div class="card" style="width: 18rem;">
            <img class="card-img-top" src="https://i.ibb.co/Rp6pXB3/Whats-App-Image-2022-04-23-at-5-07-58-PM.jpg" alt="Aruvi">
            <div class="card-body">
                <h5 class="card-title">Aruvi Puhazhendhi</h5>
                <p class="card-text">I love machine learning and have been working with neural network based computer vision for quite some time. Apart from ML I also find compiler and programming language design very interesting and spend some time with low-level systems programming.</p>
                <a href="https://github.com/aruvi-p" class="btn" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" style="width: 50px; height: 50px;">
                </a>
            </div>
        </div>

        <div class="card" style="width: 18rem; margin-left: 30px;">
            <img class="card-img-top" src="https://frankhart2017.github.io/portfolio/img/dp.jpg" alt="Siddhartha">
            <div class="card-body">
                <h5 class="card-title">Siddhartha D. Choudhury</h5>
                <p class="card-text">I love machine learning and have been working with neural network based computer vision for quite some time. Apart from ML I also find compiler and programming language design very interesting and spend some time with low-level systems programming.</p>
                <a href="https://github.com/frankhart2018" class="btn" target="_blank">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" style="width: 50px; height: 50px;">
                </a>
            </div>
        </div>
    </div>
    """,
    height=800,
)