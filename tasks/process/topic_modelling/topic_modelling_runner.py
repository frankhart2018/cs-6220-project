import os

from tasks.process.task_runner import TaskRunner
from tasks.process.topic_modelling.subtasks.clean_remove_stopwords import CleanRemoveStopwords
from tasks.process.topic_modelling.subtasks.build_dump_model import BuildDumpModel


class TopicModellingRunner(TaskRunner):
    def __init__(self, subtasks):
        self.__subtasks = subtasks

    def run(self, **kwargs):
        os.makedirs("data", exist_ok=True)

        for subtask in self.__subtasks:
            subtask_name = subtask.replace("_", " ").title().replace(" ", "")
            sub_task_obj = eval(subtask_name)()
            sub_task_obj.run(**kwargs)

