import streamlit as st
import plotly.express as px
import pandas as pd
import pickle


def read_pickle(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


def match_genre(grouped_genres, genre):
    genre_match = grouped_genres[genre]
    genre_match_tup = [(genre, count) for genre, count in genre_match.items()]
    genre_match_df = pd.DataFrame(genre_match_tup, columns=['Genre', 'Number of movies'])

    fig = px.bar(genre_match_df, x='Genre', y='Number of movies', title=f"Top 5 matches for {genre}",
                 width=1200, height=600)
    st.plotly_chart(fig)


st.set_page_config(
    layout="wide",
    page_title="Genre Popularity",
)

st.title("Most popular genres")

grouped_genres = read_pickle("data/grouped_genres_dict")
genre_count = read_pickle("data/genre_count_dict")

genre_count_tup = [(genre, count) for genre, count in genre_count.items()]
genre_count_df = pd.DataFrame(genre_count_tup, columns=["Genre", "Number of movies"])

fig = px.bar(genre_count_df, x="Genre", y="Number of movies", title="Genre popularity",
             width=1200, height=600)
st.plotly_chart(fig)

st.markdown("###### And the most popular genre is: :drum_with_drumsticks: :drum_with_drumsticks: :drum_with_drumsticks:")
st.markdown("#### Adventure, with 432 movies in it.")

st.title("Match me up")

st.write("Let's now see which genres occur together the most")

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
genre = st.radio(
     "What's your favorite movie genre",
     genre_count.keys())

match_genre(grouped_genres, genre)
