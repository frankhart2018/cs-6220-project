import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    layout="wide",
    page_title="Distributor Sales",
)

df = pd.read_csv("movies_filled_cleaned_processed.csv")

show_info = st.checkbox("Show details")

if show_info:
    st.markdown("""
**Who are movie distributors?**

Movie distributors are the companies that make movies and distribute them to the public.
    
**What do these plots mean and how are they generated?**

These plots show the distribution of the sales of movies by distributor. There are three different
plots here, each one showing the distribution of sales all distributors on world, international,
and domestic levels.
    """)
else:
    st.write("")

st.markdown("### Guess who's the most successful distributor?")
st.markdown("Check out the plots to find out!")

st.title("Distributor Sales (World)")
df.groupby(by = ["Distributor"])['World Sales (in $)'].sum().reset_index()
fig = px.pie(
    df,
    values='World Sales (in $)',
    names="Distributor",
    title='Percentage of Different Distributor in Total world Sales',
    color_discrete_sequence=px.colors.sequential.RdBu,
    width=1200,
    height=600
)
st.plotly_chart(fig)

st.title("Distributor Sales (Domestic - US)")
df.groupby(by=["Distributor"])['Domestic Sales (in $)'].sum().reset_index()
fig = px.pie(
    df,
    values='Domestic Sales (in $)',
    names="Distributor",
    title='Percentage of Different Distributor in Domestic Sales',
    color_discrete_sequence=px.colors.sequential.RdBu,
    width=1200,
    height=600
)
st.plotly_chart(fig)

st.title("Distributor Sales (International)")
df.groupby(by=["Distributor"])['International Sales (in $)'].sum().reset_index()
fig = px.pie(
    df,
    values='International Sales (in $)',
    names="Distributor",
    title='Percentage of Different Distributor in International Sales',
    color_discrete_sequence=px.colors.sequential.RdBu,
    width=1200,
    height=600
)
st.plotly_chart(fig)

st.write("If you guessed, **Walt Disney** is the most successful distributor, then congratulations you are right!")
