import pandas as pd

from tasks.clean_fill.clean.cleaner import Cleaner


class RunningTimeMins(Cleaner):
    def __get_min_from_time_string(self, time_string: str) -> int:
        hr_splits = time_string.split("hr")

        hr = int(hr_splits[0].strip())

        minutes = 0
        if hr_splits[1] != '':
            minutes = int(hr_splits[1].split("min")[0].strip())

        return hr * 60 + minutes

    def clean(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe["running_time_mins"] = dataframe["Movie Runtime"].apply(self.__get_min_from_time_string)

        return dataframe
