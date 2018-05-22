import logging
import requests
import bs4
import time
import mysql.connector as mysqldb
from article import Article

logging.basicConfig(filename='crawler.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def scrapeArticleUrlsFromPage():
    """
    Appends list of articles URLs from soup object
    """

    logging.debug("Scraping page for article titles and URLs...")
    urls = []

    try:
        res = requests.get('https://zenhabits.net/archives/')
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        elements = soup.find('table')
        article_urls = elements.select('a')

        for a in article_urls:
            urls.append(a.attrs['href'])

        return urls

    except Exception as exc:
        logging.error(exc)


def buildArticleDictionary():
    """
    Builds a dictionary for all archived articles (article URL as key)
    """

    logging.debug("Building dictionary...")
    urls = scrapeArticleUrlsFromPage()
    articles = {}

    try:

        for url in urls:
            res = requests.get(url)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            # Firstly, get article title
            title = soup.find('h2').text

            # Secondly, in order to easier parse the soup object we specify our search to the "post" itself
            elements = soup.find("div", class_="post")
            content = elements.text

            # Thirdly, get the publication date (this will subsequently be formatted in the Article object)
            date_body = soup.find("div", class_="navigation")
            date_published = date_body.find('p').text

            articles[url] = Article(url, title, date_published, content)
            time.sleep(3)

        return articles

    except Exception as exc:
        logging.error(exc)

    def saveArticleDictionary(self):
        """
        Saves article dictionary to DB
        """
        config = {'user': 'root', 'password': 'eIhuJk-dq2Jd', 'host': '127.0.0.1', 'database': 'zen_grams',
                  'raise_on_warnings': True, 'use_pure': False}
        try:
            conn = mysqldb.connect(**self.config)
            cursor = conn.cursor()
        except Exception as exc:
            logging.error(exc)
        finally:
            cursor.close()
            conn.close()

        raise NotImplementedError

    def saveNgrams(self):
        """
        Saves article N-grams to a JSON file
        """
        raise NotImplementedError
