import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import linear_kernel
import pickle

from tasks.process.task_runner import TaskRunner


class ComputeSimilarityMatrixNn(TaskRunner):
    def run(self, **kwargs):
        required_args = ["df", "similarity_matrix_path_nn", "df_mapping_path_nn", "embeddings_path"]
        self._required_args_checker(kwargs, required_args)

        df = kwargs["df"]

        embeddings = np.load(kwargs["embeddings_path"])

        similarity_matrix = linear_kernel(embeddings, embeddings)
        df_mapping = pd.Series(df.index, index=df['Title'])

        np.save(kwargs["similarity_matrix_path_nn"], similarity_matrix)

        with open(kwargs["df_mapping_path_nn"], "wb") as f:
            pickle.dump(df_mapping, f)