import requests
from bs4 import BeautifulSoup
from AppSettings import AppSettings
from typing import List


class WebScrapper:
    def __init__(self, parser: str = AppSettings.PARSER):
        self.__url = None
        self.__parser = parser
        self.__soup_client = None
        self.__web_content = None

    
    def read_product_info(self, device_type: str, size: int) -> List[tuple]:
        self.__read_website_content(device_type, size)
        return list(self.__filter_values()[0:size])


    def __filter_values(self) -> List[tuple]:
        result = []
        anty_duplicate_list = []

        for record in self.__web_content:
            price = record.find('span', attrs={'class': '_9c44d_1zemI'}).text
            transaction_count = record.find('span', attrs={'class': '_9c44d_2o04k'}).text
            duplicate_condition = True if price in anty_duplicate_list else False

            if not price or not transaction_count or duplicate_condition:
                continue
            anty_duplicate_list.append(price)
            result.append((price.strip().split('z')[0], transaction_count.split(' ')[0]))

        return result


    def __read_website_content(self, device_type: str, size: int):
        self.__url = AppSettings.URLS[device_type]
        self.__web_content = requests.get(self.__url).content
        self.__initialize_soap()
        self.__web_content = self.__soup_client.find_all('div', attrs={'class': '_9c44d_1V-js'})[0:size * 5]


    def __initialize_soap(self):
        if not self.__soup_client:
            self.__soup_client = BeautifulSoup(self.__web_content, self.__parser)



