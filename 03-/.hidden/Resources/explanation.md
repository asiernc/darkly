# Bug Report - robots.txt web scrapping /.hidden

##  Bug description

Robots.txt is a file that tells google what to index to find it with the search engines or not, however, for an attacker, it can give clues about some directories that have been avoided, but that should have been protected (in theory).

## How did I find it?

If we enter the url => http://127.0.0.1:3000/robots.txt we see two directories, /whatever and /.hidden; if we enter url/.hidden/ we find a directory, 
with many subdirectories and README files trolls. We must imagine that we have gained access to a folder that was not wanted to be shown, neither to enter by the path, but we have
obtained it because there is no url validation. Here we could start a manual search but it would take a long time, we make use of Scrapy, a python web scrapper.

## Steps to replicate

1. python3 -m venv .
2. pip install Scrapy
3. run 'scrapy crawl readme_spider' and wait for result.log file.

