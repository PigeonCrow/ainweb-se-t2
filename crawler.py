import requests
from bs4 import BeautifulSoup

# Defne request to url -->  GET
url = "https://vm009.rz.uos.de/crawl/index.html"
response = requests.get(url)
sub_urls = []

# process with bs4
soup = BeautifulSoup(response.content, "html.parser")

# parse requests
title = soup.find("h1")
paragraph = soup.find("p")
links = soup.find_all("a")

# create full urls with links
for link in links:
    addr = link.get("href")
    base_url = url.rsplit('/', 1)[0]
    sub_urls.append(base_url + "/" + addr)


print(f"Title: {title.text}")
print("\n")
print(f"Paragraph: {paragraph.text}")
print("\n")

# print(sub_urls)
for i in range(len(links)):
    print(f"link {i}: {links[i]}: {sub_urls[i]}")

# for l in links:
#    print(f"link: {l.text}")
#    addr = l.get("href")
#    print(f"address: {addr}")
