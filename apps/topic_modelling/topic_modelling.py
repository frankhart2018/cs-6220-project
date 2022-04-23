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

    components.html(lda_html, height=1000)


if __name__ == '__main__':
    main()