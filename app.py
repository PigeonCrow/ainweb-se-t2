from flask import Flask, request, render_template
from search import init_search, search
from crawler import init_set_up
import traceback


# building the flask app
app = Flask(__name__)
# ix = open_dir("index_dir")


# config setup
# DEFAULT_CONFIG = {
#    "root_url": "https://vm009.rz.uos.de/crawl/index.html",
#   "periodic_crawl": False
# }

# def load_config():
#    if os.path.exists("config.json"):
#    with open("config.json", "r") as file:
#        return json.load(file)
# else:
#    print("Config file not found. Using defaults.")
#    return DEFAULT_CONFIG


# initiazie app
# def init_set_up():
#    print("Setting UP SE ....")

#    url = load_config.root_url
#    if not os.path.exists("index_dir/"):
#        os.makedirs("index_dir")
#
#    print("setting up Index .....")
#
#    # define schema
#    schema = Schema(
#        url=ID(stored=True),
#        title=TEXT(stored=True),
#        teaser=TEXT(stored=True),
#        content=TEXT,
#    )
#
#    # generate the index
#    ix = create_in("index_dir", schema)
#
#    # Initialize writer and visited_urls set
#    writer = ix.writer()
#    visited_urls = set()
#
#    # Start the crawling process
#    crawl(url, url, visited_urls, writer)  # perform crawling once while setting up
#
#    # Commit the changes to the index
#    writer.commit()

#    if periodic_crawl:
#    start_periodic_crawl() # start periodic crawling if enabled


# home route of the flask app
@app.route("/")
def home():
    return render_template("home.html")


# search route of the flask app
@app.route("/search")
def search_route():
    query_text = request.args.get("q", "")  # get the search query
    if query_text:
        result_data = search(query_text)  # call the search function from crawler.py
        return render_template(
            "search.html", query=query_text, results=result_data
        )  # render the template using the query that was put in
    else:
        return render_template(
            "search.html", query=None, results=None
        )  # render the template without having a query -> "no results found"


## for debug
# import traceback
@app.errorhandler(500)
def internal_error(exception):
    return "<pre>" + traceback.format_exc() + "</pre>"


if __name__ == "__main__":
    # initialize crawler and write index
    init_set_up()
    # initialize search
    init_search()
    app.run(debug=True)
