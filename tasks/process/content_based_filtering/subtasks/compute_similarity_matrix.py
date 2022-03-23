import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle

from tasks.process.task_runner import TaskRunner


class ComputeSimilarityMatrix(TaskRunner):
    def run(self, **kwargs):
        required_args = ["df", "similarity_matrix_path", "df_mapping_path"]
        self._required_args_checker(kwargs, required_args)

        df = kwargs["df"]

        tfidf = TfidfVectorizer(stop_words='english')
        overview_matrix = tfidf.fit_transform(df['Movie Info'])

        similarity_matrix = linear_kernel(overview_matrix, overview_matrix)
        df_mapping = pd.Series(df.index, index=df['Title'])

        np.save(kwargs["similarity_matrix_path"], similarity_matrix)

        with open(kwargs["df_mapping_path"], "wb") as f:
            pickle.dump(df_mapping, f)