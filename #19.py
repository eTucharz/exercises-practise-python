'''
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
'''

import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")


def get_article_paragraphs(soup):
    for div in soup.find_all('div', class_='body__inner-container'):
        for p in div.find_all('p'):
            print(p.get_text().strip() + "\n")


article_paragraphs = get_article_paragraphs(soup)

print(article_paragraphs)
