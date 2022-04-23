import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    layout="wide",
    page_title="International v/s Domestic Sales",
)

df = pd.read_csv("movies_filled_cleaned_processed.csv")

show_info = st.checkbox("Show details")

if show_info:
    st.markdown("""
**Who are movie distributors?**

Movie distributors are the companies that make movies and distribute them to the public.
    
**What do these plots mean and how are they generated?**

These plots show the distribution of the sales of movies by distributor and genre. There are five different
plots here, each one showing the distribution of sales all distributors on world, international,
and domestic levels and on the basis of genre at international and domestic levels.
    """)
else:
    st.write("")

st.markdown("### Guess who's the most successful distributor and what's the most popular genre?")
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

data_g = df[['Genre','Domestic Sales (in $)','International Sales (in $)']]

data_g['Genre'] = data_g['Genre'].str.replace("'", "").str.replace("]", "").str.replace("[", "").str.replace(" ", "").str.split(',')
data_g = data_g.explode('Genre')

st.title("Genre Sales (International)")
data_g.groupby(by = ["Genre"])['International Sales (in $)'].sum().reset_index()
fig = px.pie(
    data_g,
    values='International Sales (in $)',
    names="Genre",
    title='Percentage of Different Genre in International Sales (in $)',
    color_discrete_sequence=px.colors.sequential.RdBu,
    width=1200,
    height=600
)
st.plotly_chart(fig)

st.title("Genre Sales (Domestic)")
data_g.groupby(by = ["Genre"])['Domestic Sales (in $)'].sum().reset_index()
fig = px.pie(
    data_g,
    values='Domestic Sales (in $)',
    names="Genre",
    title='Percentage of Different Genre in DOmestic Sales (in $)',
    color_discrete_sequence=px.colors.sequential.RdBu,
    width=1200,
    height=600
)
st.plotly_chart(fig)

st.write("It's **adventure**! Did you guess it right?")