import logging
import re
import datetime
import json
from calendar import month_name

logging.basicConfig(filename='article.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


class Article(object):

    def __init__(self, _url, _title, _date_published, _content):
        self.url = _url
        self.title = _title
        self.date_published = self.changeDateFormat(_date_published)
        self.content = _content

    def changeDateFormat(self, unmodified_date):
        """
        zen habits post the publication date like so: "Posted: Day of the week, <Month Name> <Date>, <Year>'
        """
        # First step is therefore to find this w/ a regex
        pattern = r"(?:%s) \d{1,2}, \d{4}" % '|'.join(month_name[1:])
        date_regex = re.search(pattern, unmodified_date)

        #  Second step is then to convert our match w/ strftime function and return it in following format 'YYYY-MM-DD'
        if date_regex:
            modified_date = datetime.datetime.strptime(date_regex.group(), '%B %d, %Y').strftime('%Y-%m-%d')
            return modified_date
        else:
            logging.error('Date cannot be formatted')

    def getNgrams(self):
        raise NotImplementedError

    def to_json(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return '{0} {1} {2}'.format(self.url, self.title, self.date_published)
