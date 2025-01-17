from flask import Flask, request, render_template, url_for
from search import init_search, search  # change for server deployment
import traceback

# globally initialize search
init_search()

# building the flask app
app = Flask(__name__)


# home route of the flask app
@app.route("/")
def home():
    return render_template("home.html")


# fixing root urls ref
@app.route("/user/u016")
def profile(username):
    return f"User: {username}"


# search route of the flask app
@app.route("/search")
def search_route():
    query_text = request.args.get("q", "")  # get the search query
    if query_text:
        result_data = search(query_text)  # call the search function
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
    # initialize search
    # init_search()
    app.run(debug=True)
