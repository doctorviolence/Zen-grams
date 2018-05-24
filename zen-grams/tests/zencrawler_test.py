import unittest
from typing import Dict
import zencrawler
from article import Article


class ZenCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.crawler = zencrawler

    def testWriteArticlesToFile(self):
        articles: Dict[str, Article] = {
            'http://www.test.com': Article('http://www.test.com', 'Test', 'Monday May 15, 2018', 'Blah blah blah'),
            'http://www.test2.com': Article('http://www.test2.com', 'Test2', 'Monday June 1, 2012', 'Sample content')
        }

        self.assertTrue(self.crawler.writeArticlesToFile(articles))
        self.assertFalse(self.crawler.writeArticlesToFile('Test'))

    def tearDown(self):
        self.crawler = None
