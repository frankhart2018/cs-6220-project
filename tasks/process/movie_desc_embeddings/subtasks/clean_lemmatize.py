import re
from tqdm import tqdm
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


from tasks.process.task_runner import TaskRunner


class CleanLemmatize(TaskRunner):
    def __init__(self):
        self.__lemmatizer = WordNetLemmatizer()

    def __lemmatize_sentence(self, sentence):
        lemmatized_sentence = ""
        for word in sentence.split():
            if len(word) <= 2 or word in stopwords.words('english'):
                continue

            lemmatized_sentence += self.__lemmatizer.lemmatize(word) + " "

        return lemmatized_sentence.strip()

    def run(self, **kwargs):
        required_args = ["df"]
        self._required_args_checker(kwargs, required_args)

        df = kwargs["df"]
        alpha_numeric_re = re.compile(r"[^a-zA-Z0-9 ]")

        movie_infos = df.iloc[:, 1].tolist()
        movie_infos_cleaned = []

        for movie_info in tqdm(movie_infos, desc="Cleaning and lemmatizing movie infos"):
            movie_info_cleaned = re.sub(alpha_numeric_re, "", movie_info.strip().lower())
            movie_info_cleaned = self.__lemmatize_sentence(sentence=movie_info_cleaned)
            movie_infos_cleaned.append(movie_info_cleaned)

        df.iloc[:, 1] = movie_infos_cleaned
