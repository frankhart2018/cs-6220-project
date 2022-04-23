import random
import re
import pandas as pd
import ntlk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import streamlit as st


ntlk.download('stopwords')
stop_words = set(stopwords.words('english'))


def text_clean(text):
    # whitespaces
    text = ' '.join(text.split())
    # everything other than alphabets
    text = re.sub("[^a-zA-Z]", " ", text)
    # backslash-apostrophe
    text = re.sub("\'", "", text)
    # text to lowercase
    text = text.lower()
    return text


def stopwords(text):
    clean_text = [i for i in text.split() if not i in stop_words]
    return ' '.join(clean_text)


def prediction(i, threshold=0.3):
    movies = pd.read_csv('movies_filled_cleaned_processed.csv')
    movies_g = movies[['Genre', 'Movie Info']]
    for i, col in enumerate(movies_g.columns):
        movies_g.iloc[:, i] = movies_g.iloc[:, i].str.replace("'", "")
        movies_g.iloc[:, i] = movies_g.iloc[:, i].str.replace("[", "")
        movies_g.iloc[:, i] = movies_g.iloc[:, i].str.replace("]", "")

    movies_g['Genre'] = movies_g['Genre'].str.split(',')

    movies = movies_g

    movies['Movie Info Clean'] = movies['Movie Info'].apply(lambda x: text_clean(x))

    movies['Movie Info Clean'] = movies['Movie Info Clean'].apply(lambda x: stopwords(x))

    multilabel_binarizer = MultiLabelBinarizer()
    multilabel_binarizer.fit(movies['Genre'])

    # transform target variable
    y = multilabel_binarizer.transform(movies['Genre'])

    tfidf_vec = TfidfVectorizer(max_df=0.8, max_features=10000)

    # split moviesset into training and validation set
    Xtrain, Xval, Ytrain, Yval = train_test_split(movies['Movie Info Clean'], y, test_size=0.2, random_state=9)

    # create TF-IDF features
    Xtrain_tfidf = tfidf_vec.fit_transform(Xtrain)
    Xval_tfidf = tfidf_vec.transform(Xval)

    lr = LogisticRegression()
    ovrclf = OneVsRestClassifier(lr)
    ovrclf.fit(Xtrain_tfidf, Ytrain)

    # threshold = 0.3 # threshold value
    y_pred_prob = ovrclf.predict_proba(Xval_tfidf)
    y_pred = (y_pred_prob >= threshold).astype(int)

    # evaluate
    f1 = f1_score(Yval, y_pred, average="micro")

    pred = multilabel_binarizer.inverse_transform(y_pred)[i]

    # returns the genre predictions
    return pred, f1


def main():
    st.set_page_config(
        page_title="Genre Prediction",
    )

    st.title("Genre Prediction")

    st.markdown("""
    ### Note
    
    The data we had was inefficient for the model, and hence the bad results. 
    """)

    show_info = st.checkbox("Show details")

    if show_info:
        st.markdown("""
    **How are predicting genre?**

    The genres are converted to integers using the MultiLabelBinarizer. Then a TfIdf vectorizer is used to create 
    TF-IDF features. Finally we train a Logistic Regression model. As you can see the predictions are same for 
    all the movies. This is also reflected in the low **F1** score. 
        """)
    else:
        st.write("")

    df = pd.read_csv("movies_filled_cleaned_processed.csv")

    movie_titles_tup = tuple(["--Select a movie--"] + df['Title'].tolist())

    movie_name = st.selectbox(
        "Select a movie",
        movie_titles_tup
    )
    if movie_name != "--Select a movie--":
        movie_idx = df.loc[df['Title'] == movie_name].index.values[0]
        pred, f1 = prediction(movie_idx)
        st.write(f"Possible genres for {movie_name} are: {pred}")
        st.write(f"F1 score: {round(f1, 2)}")

        random_threshold = random.uniform(0, 0.5)

        prediction(movie_idx, threshold=random_threshold)

if __name__ == '__main__':
    main()