import logging
import requests
import bs4
import time
import json
from article import Article

logging.basicConfig(filename='crawler.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def scrape_article_urls_from_page():
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


def build_article_dictionary():
    """
    Builds a dictionary for all archived articles (article URL as key)
    """
    logging.debug("Building dictionary...")
    urls = scrape_article_urls_from_page()
    article_dictionary = {}

    try:

        for url in urls:
            res = requests.get(url)

            if res.status_code == 200:
                soup = bs4.BeautifulSoup(res.text, "html.parser")
                elements = soup.find("div", class_="post")
                content = elements.text
                date_body = soup.find("div", class_="navigation")
                date_published = date_body.find('p').text

                article_dictionary[url] = Article(url, date_published, content)

                time.sleep(1)

        logging.debug("Article dictionary complete...")
        write_articles_to_file(article_dictionary)

    except Exception as exc:
        logging.error(exc)


def write_articles_to_file(article_dictionary):
    """
    Writes article dictionary to a JSON file
    """
    try:
        logging.debug("Writing article to JSON file...")
        article_json = {k: v.to_json() for k, v in article_dictionary.items()}

        with open('articles.json', 'w') as fp:
            json.dump(article_json, fp, sort_keys=True, indent=2, separators=(',', ':'))

        logging.debug("Articles written to JSON file...")
        return True
    except TypeError as exc:
        logging.error(exc)
        return False


def load_articles_from_file():
    """
    Loads articles from JSON file
    """
    articles = {}
    try:
        logging.debug("Loading articles from JSON file...")

        with open('articles.json') as fp:
            json_dict = json.load(fp)
            print(json_dict)

            for k, v in json_dict.items():
                article = Article(k, v['date_published'], v['content'], False)
                articles[k] = article

        logging.debug("Articles loaded from JSON file...")
        return articles

    except TypeError as exc:
        logging.error(exc)
        return None
