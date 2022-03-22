import pandas as pd

from tasks.clean_fill.clean.cleaner import Cleaner


class RemoveUnnamed(Cleaner):
    def clean(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        return dataframe.drop(columns=["Unnamed: 0"])
