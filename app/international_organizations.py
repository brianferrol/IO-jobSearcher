from app.base_scrapper import BaseScrapper
import pandas as pd
from datetime import date



class InternationalOrganizationsScrapper:
    """
    Scrapping class with one function for each IO.
    """

    def __init__(self):
        self.job_list = pd.DataFrame()

    def save_file(self, path):

        today = date.today().strftime("%d-%m-%Y")
        filename = "jobList_{}.xlsx".format(today)

        self.job_list.to_excel(path+filename, encoding="utf-8")
        return print("job list saved on {}".format(path+filename))

    def OCSE(self):
        url = "https://jobs.osce.org/vacancies?f%5B0%5D=duty_station%3AVienna"
        soup = BaseScrapper(url=url).scrap()
        results = soup.find(id='block-mainpagecontent')

        job_elems = results.find_all('div', attrs={'class': 'teaser__content'})

        for job in job_elems:
            job_url = job.find("a", href=True)["href"]
            title = job.find("a", href=True).text
            self.job_list = self.job_list.append(
                {"title": title, "job_url": "https://jobs.osce.org" + job_url},
                ignore_index=True)
