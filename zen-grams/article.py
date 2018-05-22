import logging
import re

logging.basicConfig(filename='article.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


class Article(object):
    url = None
    title = None
    date_published = None
    content = None

    def __init__(self, _url, _title, _date_published, _content):
        self.url = _url
        self.title = _title
        self.date_published = self.changeDateFormat(_date_published)
        self.content = _content

        # self.getNgrams()

    def changeDateFormat(self):
        raise NotImplementedError

    def getNgrams(self):
        raise NotImplementedError
