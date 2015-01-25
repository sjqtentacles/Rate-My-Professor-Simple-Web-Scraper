# Rate-My-Professor-Simple-Web-Scraper
Simple web scraper for Rate My Professors that gathers the very basic information from all professors of one university.


The query url is taken from "Inspect Element" on Chrome (the "network" tab after clicking on the "Load More" button on the page which lists the professors).
By going through each page (I put 210 just to make sure I got everything) I was able to collect the simple data for each professor.

This can be extended further to go to each professor's page for more information such as the chilly pepper etc.

The code uses a database for storage, MongoDB, but you can just save it to a file or some other database.
