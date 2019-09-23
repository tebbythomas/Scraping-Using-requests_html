'''
Description:
Python 3 simple scraper using the requests_html library to scrape a simple html file
'''
import csv
from requests_html import HTML, HTMLSession

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render()

match = html.find('#footer', first=True)
print(match.html)
