from sklearn.manifold import TSNE
from tqdm import tqdm
import numpy as np

from tasks.process.task_runner import TaskRunner


class GetTsneCoords(TaskRunner):
    def run(self, **kwargs):
        required_args = ["n_components", "init", "embeddings_path", "tsne_x_path", "tsne_y_path"]
        self._required_args_checker(kwargs, required_args)

        embeddings = np.load(kwargs["embeddings_path"], allow_pickle=True)

        tsne = TSNE(n_components=kwargs["n_components"], init=kwargs["init"])
        embeddings_red = tsne.fit_transform(embeddings)

        x = []
        y = []

        for embedding_red in tqdm(embeddings_red, desc="Saving TSNE coordinates"):
            x.append(embedding_red[0])
            y.append(embedding_red[1])

        np.save(kwargs["tsne_x_path"], np.array(x))
        np.save(kwargs["tsne_y_path"], np.array(y))