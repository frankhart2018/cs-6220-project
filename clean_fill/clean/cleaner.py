from abc import abstractmethod
import pandas as pd


class Cleaner:
    @abstractmethod
    def clean(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        ...
