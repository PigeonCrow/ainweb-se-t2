import requests
from bs4 import BeautifulSoup
from whoosh.index import create_in
from whoosh.fields import *
import os
from whoosh.qparser import QueryParser

# Defne request to url --> GET
url = "https://vm009.rz.uos.de/crawl/index.html"
response = requests.get(url)
sub_urls = []

# process with bs4
soup = BeautifulSoup(response.content, "html.parser")

# parse requests
title = soup.find("h1")
paragraph = soup.find("p")
links = soup.find_all("a")

# create index using whoosh
# schema for the index
schema = Schema(url=ID(stored=True), content=TEXT)

# index directory
if not os.path.exists("index_dir"):
    os.makedirs("index_dir")

# generate the index
ix = create_in("index_dir", schema)

#### indexing
# get text content for indexing
page_content = soup.get_text()

# index the content
writer = ix.writer()
writer.add_document(url=url, content=page_content)
writer.commit()

# create full urls with links
for link in links:
    addr = link.get("href")
    base_url = url.rsplit("/", 1)[0]

    sub_urls.append(base_url + "/" + addr)
    sub_response = requests.get(sub_urls[-1])
    sub_soup = BeautifulSoup(sub_response.content, "html.parser")
    sub_content = sub_soup.get_text()

    writer = ix.writer()
    writer.add_document(url=sub_urls[-1], content=sub_content)
    writer.commit()


## search for text
def search(query_text):
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_text)
        results = searcher.search(query)
        return [(result["url"]) for result in results]


print(f"Title: {title.text}")
print("\n")
print(f"Paragraph: {paragraph.text}")
print("\n")

# print(sub_urls)
for i in range(len(links)):
    print(f"link {i}: {links[i]}: {sub_urls[i]}")


# search 1
print(search("scientists"))

# search 2
print(search("Senat"))

# search 3
print(search("pixels"))


# for l in links:
#    print(f"link: {l.text}")
#    addr = l.get("href")
#    print(f"address: {addr}")
