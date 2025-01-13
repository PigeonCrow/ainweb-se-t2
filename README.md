crawler.py:
The crawl function visits the web pages starting from the specified url. It skips pages if they have different domains or were visited already and only looks at HTML pages.
BeautifulSoup is used to parse the content.
Besides the URL, also the title and the teaser are being extracted to use later in the templates.
The schema defines the fields url, title, teaser and content which are then stored in the generated index.
The search function is then takes a query and searches the indexed content. IT returns the search results including title, teaser and url.
(To test the search, three searches with different queries / search terms are done.)


app.py:
Creating the frontend;In the app.py the actual Flask web application is created, consisting of the two app routes:1. „/„ -> home
The home route uses the template „home.html“ when called to display the search form.
2. „/search“ -> search
The search route takes the query parameter q, uses the search function of the crawler.py and displays the search results by giving it to the template.
If there is no search query, the template will also be rendered, but without a query, so the results will be „No results found“.

Templates:
	home.html:
home.html contains a search form, the input field and the information what and in which way to display this and the entire home page.
	search.html:
The search.html contains all the information how and in which way to display the results.

In index_dir, the indexed data is stored. It is used for the search to compare with the search term.