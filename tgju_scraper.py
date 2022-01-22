import requests
from bs4 import BeautifulSoup
import time


class Tgju:
    def __init__(self):
        self.headers = {
            "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"""
        }
        self.url = r"https://www.tgju.org/"
        self.response = requests.get(url=self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.prices = [
            div.text for div in self.soup.find_all("span", class_="info-price")
        ]
        self.fetch_time = time.time()
        for i, _ in enumerate(self.prices):
            last_price = self.prices.pop()
            self.prices.insert(i, float(last_price.replace(",", "")))

    def get_gold_18(self):
        return self.prices[5]

    def get_gold_coin(self):
        return self.prices[4]

    def get_tether(self):
        return self.prices[1]

    def get_bitcoin(self):
        return self.prices[0]

    def get_all(self):
        prices_dict = {}
        prices_dict["gold_18"] = self.prices[5]
        prices_dict["gold_coin"] = self.prices[4]
        prices_dict["tether"] = self.prices[1]
        prices_dict["bitcoin"] = self.prices[0]
        return prices_dict
