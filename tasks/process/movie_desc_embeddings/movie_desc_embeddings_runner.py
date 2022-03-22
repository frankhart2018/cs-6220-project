import numpy as np
import os
import shutil

from tasks.process.task_runner import TaskRunner
from tasks.process.movie_desc_embeddings.subtasks.clean_lemmatize import CleanLemmatize
from tasks.process.movie_desc_embeddings.subtasks.get_embeddings import GetEmbeddings
from tasks.process.movie_desc_embeddings.subtasks.get_tsne_coords import GetTsneCoords


class MovieDescEmbeddingsRunner(TaskRunner):
    def __makedir(self, path):
        if os.path.exists(path):
            shutil.rmtree(path)

        os.makedirs(path)

    def run(self, **kwargs):
        if "df" not in kwargs and "embeddings_path" not in kwargs and "tsne_x_path" not in kwargs\
                and "tsne_y_path" not in kwargs:
            raise ValueError("'df', 'embeddings_path', 'tsne_x_path', and 'tsne_y_path' are required arguments!")

        df = kwargs["df"]

        self.__makedir(path="data")

        tasks = ["CleanLemmatize", "GetEmbeddings", "GetTsneCoords"]

        for task in tasks:
            sub_task_obj = eval(task)()
            sub_task_obj.run(**kwargs)

