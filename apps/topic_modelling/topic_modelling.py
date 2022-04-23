import streamlit as st
import streamlit.components.v1 as components


def main():
    st.set_page_config(
        layout="wide",
        page_title="Genre Popularity",
    )

    st.title("Topic Modelling")
    with open("data/lda_dump.html", "r") as f:
        lda_html = f.read()

    show_info = st.checkbox("Show details")

    if show_info:
        st.markdown("""
    **What is topic modelling?**

    The movies info in the data frame contained a lot of raw text data. We wanted to find hidden 
    semantic structure in documents. We hence chose topic modelling which is a probabilistic way 
    to comb through massive amounts of raw text and group similar groups of documents together. 
    LDA helps achieve this by categorizing the text into a document and the words per topic which 
    are modeled based on the Dirichlet distributions and processes. LDA finds the most optimal 
    representation of the Document-Topic matrix and the Topic-Word matrix to find the most optimized 
    Document-Topic distribution and Topic-Word distribution. This helps us see the words that make up 
    each hidden topic. And ultimately this helps the user view the summary of the entire raw text data 
    in a consolidated way. Offers us a view of the words that make up each hidden topic. The uses of this 
    can grow beyond just summarization. The topics from the LDA output can be used for feature engineering 
    for prediction models.
        """)
    else:
        st.write("")

    components.html(lda_html, height=1000)


if __name__ == '__main__':
    main()