from app.base_scrapper import BaseScrapper
import pandas as pd
from datetime import date


class InternationalOrganizationsScrapper:
    """
    Scrapping class with one function for each IO.
    """

    def __init__(self):
        self.job_list = pd.DataFrame()

    @staticmethod
    def _make_hyperlink(value):
        """utility for converting value to hyperlink"""
        return '=HYPERLINK("%s", "%s")' % (value, value)

    def save_file(self, path):

        today = date.today().strftime("%d-%m-%Y")
        filename = "jobList_{}.xlsx".format(today)

        # convert column job_url value to hyperlink:
        self.job_list["job_url"] = self.job_list["job_url"].apply(lambda x: self._make_hyperlink(x))

        # order DataFrame columns (TOC):
        self.job_list = self.job_list[["title", "job_url"]]

        # save DataFrame to excel.
        self.job_list.to_excel(path + filename, encoding="utf-8", index=False)
        return print("job list saved on {}".format(path + filename))

    def OSCE(self):
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

    def UN_jobs(self):
        """
        This website presents a particular difficulty: as there is too many jobs, they are split in different
        pages.
        """

        # Get jobs from first page:
        url = "https://unjobs.org/duty_stations/vie"
        soup = BaseScrapper(url=url).scrap()
        job_elems = soup.find_all('div', attrs={'class': 'job'})
        for job in job_elems:
            try:
                id = job["id"]  # force error if not id
                job_url = job.find("a", href=True)["href"]
                title = job.find("a", href=True).text
                self.job_list = self.job_list.append(
                    {"title": title, "job_url": job_url},
                    ignore_index=True)
            except KeyError:
                pass

        # Get the last page of jobs:
        pages = soup.find_all("a", attrs={"class": "ts"})
        lastPage = None
        for button in pages:
            if button.text.find("Last") >= 0:
                lastPage = button["href"]

        # Once we have the number of pages, lets get every job and append it to the list:
        for num_page in range(2, int(lastPage[-1]) + 1):  # last digit shows number of page
            base_url = url + "/"
            soup = BaseScrapper(url=base_url + str(num_page)).scrap()
            job_elems = soup.find_all('div', attrs={'class': 'job'})
            for job in job_elems:
                try:
                    id = job["id"]
                    job_url = job.find("a", href=True)["href"]
                    title = job.find("a", href=True).text
                    self.job_list = self.job_list.append(
                        {"title": title, "job_url": job_url},
                        ignore_index=True)
                except KeyError:
                    pass
