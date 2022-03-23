import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd


st.set_page_config(
    layout="wide",
    page_title="Visualize PCA Embeddings",
)

st.title("PCA embeddings for movie descriptions")


x = np.load("data/pca_x.npy").tolist()
y = np.load("data/pca_y.npy").tolist()

df_movie = pd.read_csv("movies_filled_cleaned_processed.csv")
movie_names = df_movie['Title'].tolist()

show_info = st.checkbox("Show details")

if show_info:
    st.markdown("""
**What is this graph?**

We have taken the short summary of the movie's plot and converted it into high-dimensional vector,
using a pre-trained neural network model called [SentenceBert](https://www.sbert.net/) this vector is also called
embedding. The embedding that this model gives is 786-dimensional, since we are not :robot_face:, we cannot visualize
that, so PCA reduces the vector into 2 dimensions, but still maintaining the knowledge that was encoded
in those 786 dimensions as far as possible. This graph is basically a PCA reduced plot in 2 dimensions for the
786-dimensional vector.

**What does this signify?**

Well, this signifies that movies that are closer to each other have similar plots, don't believe us? Check it out
by hovering on the dots in the plot below.
    """)
else:
    st.write("")

vals = {'PCA_1': x, 'PCA_2': y, 'movie_names': movie_names}

df = pd.DataFrame(vals)

fig = px.scatter(df, x='PCA_1', y='PCA_2', hover_name='movie_names',
                 title="<b>PCA reduction for movie description embeddings</b>",
                 width=1200, height=600)
fig.update_traces(mode="markers")

st.plotly_chart(fig)