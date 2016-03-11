# jcrawler

## j-branch

## What is this?
This is just a simple python email crawler that crawls only one depth of each page. 
I uses selenium to fetch emails rather than http request, to hanlde some basic JavaScript rendering.

## This is not for:
Angular pages. 

Why? If you make it unfriendly to SEO, crawler does not help. Or say, not efficiently helpful.

How to make angular site SEO? https://www.deepcrawl.com/knowledge/best-practice/angular-js-and-seo/

## Requirements (that I use):
Python 2.7.9

Pip 6.0.7 

## Packages
<code>
pip install selenium
</code>

<code>
pip install bs4
</code>

If you have problems with selenium, for example, unable to start a browser, check http://selenium-python.readthedocs.org/ to see what you miss.

## Run Example
<code>
python crawler.py mit.edu
</code>


