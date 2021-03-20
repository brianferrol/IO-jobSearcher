import re

import requests
from bs4 import BeautifulSoup

url = "https://jobs.osce.org/vacancies/senior-auditing-assistant-vnsecg01609"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

ps = soup.findAll("p")
for p in ps:
    if p.find("strong", text="Deadline for Applications:"):
        print(p.text.split(": ")[1])

a_list = soup.findAll("li", attrs={"class": "list-group-item dropdown-toggle"})
for a in a_list:
    if a.text.find("Grade:") >= 0:
        print(a.text.split(":")[1])

cd = soup.findAll("div")
for div in cd:
    try:
        id = div["id"]
        print(div.text)
    except KeyError:
        pass

body = soup.findAll("section", attrs={"class": "content-metadata"})
dds = body[0].findAll("dd")
grade = body[0].getText().split("Grade ")[1].split("\n")[0]
for dd in dds:
    print(dd.text)

a= {}
for i in range(0, len(body[0].findAll("dd"))):
    a[body[0].findAll("dt")[i].text] = body[0].findAll("dd")[i].text.replace("\n", "")
