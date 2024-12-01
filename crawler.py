import requests
from bs4 import BeautifulSoup

# def Pull requests -->  GET
url = "https://vm009.rz.uos.de/crawl/index.html"
response = requests.get(url)
# process with bs4
soup = BeautifulSoup(response.content, "html.parser")

# parse requests
title = soup.find("h1")
paragraph = soup.find("p")
links = soup.find_all("a")

# create full urls with links


print(f"Title: {title.text}")
print("\n")
print(f"Paragraph: {paragraph.text}")
print("\n")
for l in links:
    print(f"link: {l.text}")
