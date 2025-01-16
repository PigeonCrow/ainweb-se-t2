import requests
import os
from bs4 import BeautifulSoup
from whoosh.index import create_in
from whoosh.fields import *
from urllib.parse import urljoin, urlparse

# Defne request to url --> GET
url = "https://vm009.rz.uos.de/crawl/index.html"
# response = requests.get(url)

# define index variable globally
# ix = None


## define crawler to search recursively
def crawl(url, base_url, visited_urls, writer):
    # skip if already visited or different domain
    if url in visited_urls or urlparse(url).netloc != urlparse(base_url).netloc:
        return

    # print(f"crawling: {url}")
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

        # extract the title and teaser from the crawled page
        title = soup.find("h1")
        teaser = soup.find("p")
        title_text = title.get_text(strip=True) if title else "No Title"
        teaser_text = teaser.get_text(strip=True) if teaser else "No Teaser"

        # index url
        writer.add_document(
            url=url, title=title_text, teaser=teaser_text, content=soup.get_text()
        )

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
def init_set_up():
    print("Setup SE ....")
    schema = Schema(
        url=ID(stored=True),
        title=TEXT(stored=True),
        teaser=TEXT(stored=True),
        content=TEXT,
    )

    # index directory
    if not os.path.exists("index_dir"):
        os.makedirs("index_dir")

    print("Index directory verified ....")
    global ix
    # generate the index
    ix = create_in("index_dir", schema)

    print("Index created ....")

    # Initialize writer and visited_urls set
    writer = ix.writer()
    visited_urls = set()

    # Start the crawling process
    crawl(url, url, visited_urls, writer)

    # Commit the changes to the index
    writer.commit()

    print("Index written ....")
    print("Setup completed!!")


# search for text
# def search(query_text):
#    with ix.searcher() as searcher:
#        query = QueryParser("content", ix.schema).parse(query_text)
#        results = searcher.search(query)
#        result_data = [
#            {
#                "url": result["url"],
#                "title": result.get("title", "No Title"),
#                "teaser": result.get("teaser", "No Teaser"),
#            }
#            for result in results
#        ]
#        # return results including title, teaser and url
#        return result_data


# Testing the search:
# search 1
# print(search("scientists")) #returns an URL

# search 2
# print(search("Senat")) #returns "No results found"

# search 3
# print(search("pixels")) #returns an url

# to execute crawler independently
init_set_up()
