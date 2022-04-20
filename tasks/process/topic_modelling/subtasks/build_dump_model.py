import gensim.corpora as corpora
import gensim
import pyLDAvis.gensim_models

from tasks.process.task_runner import TaskRunner


class BuildDumpModel(TaskRunner):
    def run(self, **kwargs):
        required_args = ["df", "lda_dump_path"]
        self._required_args_checker(kwargs, required_args)

        df = kwargs["df"]

        words = df["words"].values.tolist()

        id2word = corpora.Dictionary(words)
        texts = words
        corpus = [id2word.doc2bow(text) for text in texts]

        num_topics = 10
        lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                               id2word=id2word,
                                               num_topics=num_topics)
        vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word)

        pyLDAvis.save_html(vis, kwargs["lda_dump_path"])