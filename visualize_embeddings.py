import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd


st.set_page_config(
    layout="wide"
)

x = np.load("x_arr.npy").tolist()
y = np.load("y_arr.npy").tolist()


df_movie = pd.read_csv("movies_filled_cleaned_processed.csv")
movie_names = df_movie['Title'].tolist()


vals = {'tSNE_1': x, 'tSNE_2': y, 'movie_names': movie_names}

df = pd.DataFrame(vals)

fig = px.scatter(df, x='tSNE_1', y='tSNE_2', hover_name='movie_names',
                 title="<b>tSNE reduction for movie description embeddings</b>",
                 width=1200, height=600)
fig.update_traces(mode="markers")

st.plotly_chart(fig)