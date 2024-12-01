import requests
from bs4 import BeautifulSoup

# def Pull requests -->  GET
url = "https://vm009.rz.uos.de/crawl/index.html"
response = requests.get(url)

# process with bs4
soup = BeautifulSoup(response.content, "html.parser")

# parse requests
title = soup.find("h1").text
paragraph = soup.find("p").text


print(f"Title: {title}")
print("\n")
print(f"Paragraph: {paragraph}")
