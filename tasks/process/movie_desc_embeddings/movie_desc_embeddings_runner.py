import os

from tasks.process.task_runner import TaskRunner
from tasks.process.movie_desc_embeddings.subtasks.clean_lemmatize import CleanLemmatize
from tasks.process.movie_desc_embeddings.subtasks.get_embeddings import GetEmbeddings
from tasks.process.movie_desc_embeddings.subtasks.get_tsne_coords import GetTsneCoords
from tasks.process.movie_desc_embeddings.subtasks.get_pca_coords import GetPcaCoords


class MovieDescEmbeddingsRunner(TaskRunner):
    def __init__(self, subtasks):
        self.__subtasks = subtasks

    def run(self, **kwargs):
        os.makedirs("data", exist_ok=True)

        for subtask in self.__subtasks:
            subtask_name = subtask.replace("_", " ").title().replace(" ", "")
            sub_task_obj = eval(subtask_name)()
            sub_task_obj.run(**kwargs)

