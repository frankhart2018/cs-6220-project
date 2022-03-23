import numpy as np
import os
import shutil

from tasks.process.task_runner import TaskRunner
from tasks.process.content_based_filtering.subtasks.compute_similarity_matrix import ComputeSimilarityMatrix


class ContentBasedFilteringRunner(TaskRunner):
    def __init__(self, subtasks):
        self.__subtasks = subtasks

    def run(self, **kwargs):
        os.makedirs("data", exist_ok=True)

        for subtask in self.__subtasks:
            subtask_name = subtask.replace("_", " ").title().replace(" ", "")
            sub_task_obj = eval(subtask_name)()
            sub_task_obj.run(**kwargs)

