'''
Use the BeautifulSoup and requests Python packages
to print out a list of all the article titles on the New York Times homepage.
'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")


def get_list_of_article_titles(soup):
    article_titles = [tag.get_text().strip() for tag in soup.find_all("h3")
                      ]
    return article_titles


artTitles = get_list_of_article_titles(soup)
