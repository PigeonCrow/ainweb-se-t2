# Search Engine: "Inert Pigeon"

<p align="center">
  <img src="static/img/pgn_logo.png" alt="inert_pigeon"/ width="200" height="200">
</p>
<p align="center">
  <em>inert pigeon flies low ...</em>
</p>




***project created in the scope of Task II, for the Seminar "AI & The Web", by Group 14*** 


## About
A small search engine, its logic is build with Python, utilising the libraries BeautifulSoup and Woosh. 
Flask framework is used to manage the webservice and for frontend design(CSS templating) Bulma(https://bulma.io/) was applied.

## Scope
The root of the search is hardcoded, limited to the test site https://vm009.rz.uos.de/crawl/index.html.


## Components

### app.py:

The app.py is the entry point of our project.
It when started initialises the created index for the Search.
It contains the actual Flask web application, consisting of the two app routes:1. „/„ -> home
The home route uses the template „home.html“ when called to display the search form.
2. „/search“ -> search
The search route takes the query parameter `q`, uses the search function of the search.py and displays the search results by giving it to the form.
If there is no search query, the template will also be rendered, but without a query, so the results will be „No results found“.

start the app
```
python app.py
```

### crawler.py:

The crawl function visits the web pages starting from the specified url.
It skips pages if they have different domains or were visited already and only looks at HTML pages.
BeautifulSoup is used to parse the content.
Besides the URL, also the title and the teaser are being extracted to use later in the templates/forms.
The schema defines the fields url, title, teaser and content which are then stored in the generated index.
The Crawler can be if included, initilised, explicitly or by another application aswell (to create/re-create the index)  

To use the crawler for a differnt site one needs just to edit the url parameter
```
url = "https://vm009.rz.uos.de/crawl/index.html"
```
In order to execute the crawler to create an index in a different location, just copy it and execute it
```
python crawler.py
```
it will initialise the whole setup again, creating an index directory and index in the process.

### search.py
contains the search function.
It takes a query and searches the indexed content. 
IT returns the search results including title, teaser and url.
(To test the search, three searches with different queries / search terms are done.)

Important here, search requires an index to point to. The initialisation process is in this context triggered by app.py.


### Templates:
 - home.html:
home.html contains a search form, the input field and the information what and in which way to display this and the entire home page.
 - search.html:
The search.html contains all the information how and in which way to display the results.

### Index Directory
In index_dir, the indexed data is stored. It is used for the search to compare with the search term.

### Static Directory
static images used 
