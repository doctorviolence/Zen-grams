import logging

class Article(object):
    url = None
    title = None
    date_published = None
    content = None

    def __init__(self, _url):
        self.url = _url
        self.title = None
        self.date_published = None
        self.content = None

        # calls method to scrape data based on article's URL
        self.scrape_data_from_page()

    def scrape_data_from_page(self):
        print(self.url, self.title)
        if self.url is None:
            raise Exception("Url already exists")

        #url = getSoupFromURL(self.url)

        try:
            # self.title =
            # self.date_published =
            # self.content =

            self.insert_data_to_db(url, title, date_published, content)

        except Exception:
            logging.error(Exception.message)

    def insert_data_to_db(self, url, title, date_published, content):

    def get_n_grams(self):
        if self.content is not None:
            # splice content into n-grams

        else:
            print("No content to splice")
