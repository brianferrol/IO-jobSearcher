import requests
from bs4 import BeautifulSoup

class BaseScrapper:
    """
    Base scrapper with utils for getting information from websites
    """

    def __init__(self, url):
        self.url = url

    def scrap(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup