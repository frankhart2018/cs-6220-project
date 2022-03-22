from abc import abstractmethod


class TaskRunner:
    @abstractmethod
    def run(self, **kwargs):
        ...