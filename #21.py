'''
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
'''

# import modules
import requests
from bs4 import BeautifulSoup

# get list of all heading from website


def get_list_of_article_headings(soup):
    article_headings = [tag.get_text().strip() for tag in soup.find_all("h3")
                        ]
    return article_headings


if __name__ == "__main__":
    # assign website to url
    url = 'https://www.nytimes.com'
    # get website and store it
    r = requests.get(url)
    # get the website's html and store it
    r_html = r.text

    # make soup
    soup = BeautifulSoup(r_html, features="html.parser")

    # call function and store list
    art_headings = get_list_of_article_headings(soup)

    # ask for file name

    file_to_save = input(
        "Write name, you want save file. For example 'my_file'")

    # open file for write
    with open(file_to_save + ".txt", 'w') as open_file:
        # iterate over list
        for heading in art_headings:
            # save each heading in file
            open_file.write(heading + "\n")
