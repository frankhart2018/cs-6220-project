import re
from nltk.corpus import stopwords
import gensim
from gensim.utils import simple_preprocess

from tasks.process.task_runner import TaskRunner


class CleanRemoveStopwords(TaskRunner):
    def __init__(self):
        self.__stop_words = stopwords.words('english')
        self.__stop_words.extend(['us', 'get', 'one', 'two', 'stop', 'from', 'subject', 're', 'for', 'then', 'must'])

    def __sent_to_words(self, para):
        for p in para:
            # deacc=True removes punctuations
            yield (gensim.utils.simple_preprocess(str(p), deacc=True))

    def __remove_stopwords(self, texts):
        return [[word for word in simple_preprocess(str(doc)) if word not in self.__stop_words] for doc in texts]

    def run(self, **kwargs):
        required_args = ["df"]
        self._required_args_checker(kwargs, required_args)

        df = kwargs["df"]

        df['Movie_Info_clean'] = df['Movie Info'].apply(lambda x: re.sub('[,!?]', '', x.lower()))
        info = df['Movie_Info_clean'].values.tolist()
        words = list(self.__sent_to_words(info))
        words = self.__remove_stopwords(words)

        df['words'] = words
