import logging
import re
import datetime
from calendar import month_name

logging.basicConfig(filename='article.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


class Article(object):

    def __init__(self, _url, _date_published, _content, modify_date=True):
        self.url = _url
        self.content = _content

        if modify_date:
            self.date_published = self.change_date_format(_date_published)
        else:
            self.date_published = _date_published

    def change_date_format(self, unmodified_date):
        """
        Zen habits post the publication date like so: "Posted: Day of the week, <Month Name> <Date>, <Year>'
        First step is therefore to find this w/ a regex
        Second step is then to convert our match w/ strftime function and return it in following format 'YYYY-MM-DD'
        """
        pattern = r"(?:%s) \d{1,2}, \d{4}" % '|'.join(month_name[1:])
        date_regex = re.search(pattern, unmodified_date)

        if date_regex:
            modified_date = datetime.datetime.strptime(date_regex.group(), '%B %d, %Y').strftime('%Y-%m-%d')
            return modified_date
        else:
            logging.error('Date cannot be formatted')

    def get_n_grams(self):
        raise NotImplementedError

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    def to_json(self):
        return self.__dict__
