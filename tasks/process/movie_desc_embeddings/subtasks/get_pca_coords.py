from sklearn.decomposition import PCA
from tqdm import tqdm
import numpy as np

from tasks.process.task_runner import TaskRunner


class GetPcaCoords(TaskRunner):
    def run(self, **kwargs):
        required_args = ["n_components", "embeddings_path", "pca_x_path", "pca_y_path"]
        self._required_args_checker(kwargs, required_args)

        embeddings = np.load(kwargs["embeddings_path"], allow_pickle=True)

        pca = PCA(n_components=kwargs["n_components"])
        embeddings_red = pca.fit_transform(embeddings)

        x = []
        y = []

        for embedding_red in tqdm(embeddings_red, desc="Saving PCA coordinates"):
            x.append(embedding_red[0])
            y.append(embedding_red[1])

        np.save(kwargs["pca_x_path"], np.array(x))
        np.save(kwargs["pca_y_path"], np.array(y))