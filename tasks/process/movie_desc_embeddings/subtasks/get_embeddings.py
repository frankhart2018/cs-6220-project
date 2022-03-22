from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import numpy as np

from tasks.process.task_runner import TaskRunner


class GetEmbeddings(TaskRunner):
    def __init__(self):
        self.__sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')

    def run(self, **kwargs):
        if "df" not in kwargs:
            raise ValueError("Missing argument: 'df'!")

        df = kwargs["df"]
        movie_infos_cleaned = df.iloc[:, 1].tolist()

        embeddings = []

        for movie_info in tqdm(movie_infos_cleaned, desc="Getting embeddings"):
            embeddings.append(self.__sbert_model.encode([movie_info])[0])

        np.save(kwargs["embeddings_path"], embeddings)

