import requests
from bs4 import BeautifulSoup
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
import os
from urllib.parse import urljoin, urlparse

# Defne request to url --> GET
url = "https://vm009.rz.uos.de/crawl/index.html"
# response = requests.get(url)


## define crawler to search recursively
def crawl(url, base_url, visited_urls, writer):
    # skip if already visited or different domain
    if url in visited_urls or urlparse(url).netloc != urlparse(base_url).netloc:
        return

    print(f"crawling: {url}")

    try:
        # get page content
        response = requests.get(url)

        # skip if not HTML (page not found)
        if "text/html" not in response.headers.get("Content-Type", ""):
            return

        # Mark as visited
        visited_urls.add(url)

        # process with bs4
        soup = BeautifulSoup(response.content, "html.parser")

        # index url
        writer.add_document(url=url, content=soup.get_text())

        # find all links
        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if href:
                # create complete links
                full_url = urljoin(url, href)

                # crawl again if not visited
                crawl(full_url, base_url, visited_urls, writer)

    except Exception as e:
        print(f"Error accessing {url}: {str(e)}")


# parse requests
# title = soup.find("h1")
# paragraph = soup.find("p")
# links = soup.find_all("a")


# create index using whoosh
# schema for the index
schema = Schema(url=ID(stored=True), content=TEXT)

# index directory
if not os.path.exists("index_dir"):
    os.makedirs("index_dir")

# generate the index
ix = create_in("index_dir", schema)

# Initialize writer and visited_urls set
writer = ix.writer()
visited_urls = set()

# Start the crawling process
crawl(url, url, visited_urls, writer)

# Commit the changes to the index
writer.commit()


# search for text
def search(query_text):
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_text)
        results = searcher.search(query)
        return [(result["url"]) for result in results]


# search 1
print(search("scientists"))

# search 2
print(search("Senat"))

# search 3
print(search("pixels"))
