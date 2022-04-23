import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm

from tasks.clean_fill.fill.filler import Filler
from tasks.clean_fill.utils.constants import IMDB_URL


class ReleaseDate(Filler):
    def __init__(self):
        self.__browser = webdriver.Chrome(ChromeDriverManager().install())

    def fill(self, **kwargs):
        if "df" not in kwargs:
            raise ValueError("df is a required field!")

        df: pd.DataFrame = kwargs["df"]
        release_dates = []

        for i, row in tqdm(df.iterrows(), desc="Filling release dates"):
            movie_name: str = row["Title"]
            if type(row["Release Date"]) == str:
                release_dates.append(row["Release Date"])
                continue

            self.__browser.get(IMDB_URL)

            search_bar = self.__browser.find_element(
                by="xpath",
                value="//input[@id='suggestion-search']",
            )
            search_bar.send_keys(movie_name)
            search_bar.send_keys(Keys.ENTER)

            movie_url = self.__browser.find_element(
                by="xpath", value="//tbody/tr[@class='findResult odd'][1]/td[2]/a"
            ).get_attribute("href")

            movie_url_split = movie_url.split("?")
            movie_release_info_url = (
                movie_url_split[0] + "releaseinfo" + "?" + movie_url_split[1]
            )
            self.__browser.get(movie_release_info_url)

            country_trs = self.__browser.find_elements(
                by="xpath",
                value="//tr[@class='ipl-zebra-list__item release-date-item']",
            )

            found_release_date = False
            for country_tr in country_trs:
                country_tds = country_tr.find_elements(by="xpath", value="./child::td")

                if country_tds[0].text == "USA":
                    release_date = country_tds[1].text
                    release_dmy = release_date.split(" ")
                    release_dates.append(
                        f"{release_dmy[1]} {release_dmy[0]}, {release_dmy[2]}"
                    )
                    found_release_date = True
                    break

            if not found_release_date:
                release_dates.append(None)

        self.__browser.close()

        df["release_date_filled"] = release_dates

        return df
