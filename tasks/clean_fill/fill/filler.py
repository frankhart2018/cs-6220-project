from abc import abstractmethod


class Filler:
    @abstractmethod
    def fill(self, **kwargs):
        ...
