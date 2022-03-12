from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from clean_fill.fill.filler import Filler
from clean_fill.utils.constants import IMDB_URL


class ReleaseDate(Filler):
    def __init__(self):
        self.__browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def fill(self, **kwargs):
        if "movie_name" not in kwargs:
            raise ValueError("movie_name is a required field!")

        movie_name = kwargs["movie_name"]

        self.__browser.get(IMDB_URL)

        search_bar = self.__browser.find_element(
            by="xpath",
            value="//input[@class='imdb-header-search__input _3gDVKsXm3b_VAMhhSw1haV react-autosuggest__input']"
        )
        search_bar.send_keys(movie_name)
        search_bar.send_keys(Keys.ENTER)

        movie_url = self.__browser.find_element(
            by="xpath",
            value="//tbody/tr[@class='findResult odd'][1]/td[2]/a"
        ).get_attribute('href')

        movie_url_split = movie_url.split('?')
        movie_release_info_url = movie_url_split[0] + 'releaseinfo' + '?' + movie_url_split[1]
        self.__browser.get(movie_release_info_url)

        country_trs = self.__browser.find_elements(
            by="xpath",
            value="//tr[@class='ipl-zebra-list__item release-date-item']"
        )

        for country_tr in country_trs:
            country_tds = country_tr.find_elements(
                by="xpath",
                value="//td"
            )

            if country_tds[0].text == 'USA':
                release_date = country_tds[1].text
                release_dmy = release_date.split(' ')
                return f"{release_dmy[1]} {release_dmy[0]}, {release_dmy[2]}"

        return 'N/A'
