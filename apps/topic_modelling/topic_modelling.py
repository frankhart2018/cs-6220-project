import pyLDAvis.gensim_models
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
import pandas as pd
import re
import streamlit as st
import streamlit.components.v1 as components


def main():
    st.set_page_config(
        layout="wide",
        page_title="Genre Popularity",
    )

    with open("data/lda_dump.html", "r") as f:
        lda_html = f.read()

    components.html(lda_html, height=1000)


if __name__ == '__main__':
    main()