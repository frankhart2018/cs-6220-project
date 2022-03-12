import pandas as pd
from typing import List, Optional

from clean_fill.clean.cleaner import Cleaner


class GetReleaseYear(Cleaner):
    def clean(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        release_year: List[Optional[int]] = []

        input_col: str = "Release Date" if "release_date_filled" not in dataframe.columns else "release_date_filled"

        for i, row in dataframe.iterrows():
            if type(row[input_col]) == str:
                release_year.append(int(row[input_col].split(",")[-1]))
            else:
                release_year.append(None)

        dataframe["release_year"] = release_year
        dataframe["release_year"] = pd.to_numeric(dataframe["release_year"])

        return dataframe
