from whoosh.index import open_dir
from whoosh.qparser import QueryParser

# init index var globally
ix = None


# init index pointer explicitly for search
def init_search():
    global ix
    ix = open_dir("index_dir")  # add reference for server deployment
    print("search initialized!!!")


def search(query_text):
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_text)
        results = searcher.search(query)

        result_data = [
            {
                "url": result["url"],
                "title": result.get("title", "No Title"),
                "teaser": result.get("teaser", "No Teaser"),
            }
            for result in results
        ]
        # return results including title, teaser and url
        return result_data
