import requests
from bs4 import BeautifulSoup

url = "https://jobs.osce.org/vacancies?f%5B0%5D=duty_station%3AVienna"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='block-mainpagecontent')

job_elems = results.find_all('div', attrs={'class': 'teaser__content'})

for job in job_elems:
    job_url = job.find("a", href=True)["href"]
    title = job.find("a", href=True).text
    print(title, job_url)