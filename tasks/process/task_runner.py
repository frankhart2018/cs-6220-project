from abc import abstractmethod


class TaskRunner:
    def _required_args_checker(self, kwargs_dict, task_runner, *args):
        for arg in args:
            if arg not in kwargs_dict:
                raise ValueError(f"{args} are required params in {self.__class__.__name__}!")

    @abstractmethod
    def run(self, **kwargs):
        ...