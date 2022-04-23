import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def time_line():
    plt.rcParams["figure.figsize"] = (17,7)
    data = pd.read_csv('movies_filled_cleaned_processed.csv')

    data_g = data[['Genre', 'release_year']]
    data_g['Genre'] = data_g['Genre'].str.replace("'", "").str.replace("]", "").str.replace("[", "").str.replace(" ", "").str.split(',')
    data_g = data_g.explode('Genre')
    data_g_grp = data_g.value_counts().to_frame('counts').reset_index()
    data_g_grp=data_g_grp.sort_values('release_year')
    data_g_grp = data_g_grp.reset_index()

    fig,ax = plt.subplots()

    for name in data_g_grp['Genre'].unique():
        ax.plot(data_g_grp[data_g_grp.Genre==name].release_year,data_g_grp[data_g_grp.Genre==name].counts,label=name)

    ax.set_xlabel("year")
    ax.set_ylabel("weight")
    ax.legend(loc='best')

    return fig


st.set_page_config(
    layout="wide",
    page_title="Genre trend over the years",
)

st.title("Genre trend over the years")

show_info = st.checkbox("Show details")

if show_info:
    st.markdown("""
**What is this graph?**

This graph shows the popularity of each genre over the years right from 1940 to 2020. The popularity is 
calculated by the number of movies that have that genre as one of their genres. The count is then plotted
on the y-axis and the years on the x-axis.
    """)
else:
    st.write("")

st.write("What's your favourite genre? Is it popular right now?")
st.write("Guess you'll find out!")

fig = time_line()
st.pyplot(fig)

st.markdown("""
### Interesting information

1. Till 1970s there are very few movies of any genre, which seems correct as the number of movies made in that time period is in fact very low. 

2. After 1980 there seems to be a boom in the number of movies, which started somewhere around mid 1970s and continues to this day, more about this can be read here [1980 in film](https://en.wikipedia.org/wiki/1980s_in_film).

3. In recent times the most popular genres are fantasy and adventure, people really tend to like these movies and hence their popularity.
""")