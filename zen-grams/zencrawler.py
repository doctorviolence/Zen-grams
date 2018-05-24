import logging
import requests
import bs4
import time
import jsonpickle
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
    article_dictionary = {}

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

            article_dictionary[url] = Article(url, title, date_published, content)

            time.sleep(3)

        logging.debug("Article dictionary complete...")
        # writeArticleDictionaryToFile(article_dictionary)

    except Exception as exc:
        logging.error(exc)


def writeArticlesToFile(article_dictionary):
    """
    Writes article to a JSON file
    """
    try:
        logging.debug("Writing article to JSON file...")
        article_json = jsonpickle.encode({url: article.to_json() for url, article in article_dictionary.items()})

        with open('articles.json', "w") as fp:
            fp.write(article_json)
            fp.close()

        return True
    except Exception as exc:
        logging.error(exc)
        return False


"""
def saveArticleDictionary(articles):
    sql_articles = 'INSERT IGNORE INTO articles(article_url, date_published, article_title) VALUES(%s, %s, %s)'

    logging.debug("Connecting to DB...")
    conn = mysqldb.connect(host="127.0.0.1", user="root", passwd="pass", db='zen_grams', )
    cursor = conn.cursor()

    try:
        logging.debug("Inserting articles to DB...")

        for key, value in articles.items():
            cursor.execute(sql_articles, (key, value.date_published, value.title))
            conn.commit()

        logging.debug("Articles saved in DB...")

        return True
    except Exception as exc:
        logging.error(exc)

        return False
    finally:
        cursor.close()
        conn.close()
"""
