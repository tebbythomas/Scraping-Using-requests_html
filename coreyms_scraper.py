'''
Description:
Python 3 scraper using the requests_html library to scrape the article information
from https://coreyms.com
'''
import csv
from requests_html import HTML, HTMLSession

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline', 'Summary', 'Video Link'])
session = HTMLSession()
r = session.get('https://coreyms.com')


articles = r.html.find('article')
for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    print("Headline:")
    print(headline + "\n")

    summary = article.find('.entry-content p', first=True).text
    print("Summary:")
    print(summary + "\n")

    yt_link = None
    try:
        vid_src = article.find('iframe', first=True).attrs['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None
    print("Youtube Link:")
    print(yt_link)
    print("\n")
    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
