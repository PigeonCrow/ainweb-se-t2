from flask import Flask, request, render_template
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from crawler import search

#building the flask app
app = Flask(__name__)
#ix = open_dir("index_dir")

#home route of the flask app
@app.route("/")
def home():
    return render_template("home.html") 

#search route of the flask app
@app.route("/search")
def search_route():
    query_text = request.args.get("q", "") 
    if query_text:
        result_html = search(query_text)  #use the search function of the crawler
        return render_template("search.html", query=query_text, results=result_html) #render the template using the query that was put in
    else:
        return render_template("search.html", query=None, results=None) #render the template without having a query -> "no results found"

if __name__ == "__main__":
    app.run(debug=True)         
