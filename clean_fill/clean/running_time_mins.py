import pandas as pd

from clean_fill.clean.cleaner import Cleaner


class RunningTimeMins(Cleaner):
    def __get_min_from_time_string(self, time_string: str) -> int:
        hr = int(time_string.split("hr")[0].strip())
        min = int(time_string.split("hr")[1].split("min")[0].strip())

        return hr * 60 + min

    def clean(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe["running_time_mins"] = dataframe["Movie Runtime"].apply(self.__get_min_from_time_string)

        return dataframe