import unittest
from typing import Dict
import zencrawler
from article import Article


class ZenCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.crawler = zencrawler
        article_one = Article('http://www.test.com', 'Monday May 15, 2018', 'Test content')
        article_two = Article('http://www.test2.com', 'Monday June 1, 2012', 'Sample content')

        self.articles: Dict[str, Article] = {
            'http://www.test.com': article_one,
            'http://www.test2.com': article_two
        }

    def test_write_articles_to_file(self):
        self.assertTrue(self.crawler.write_articles_to_file(self.articles))

    def test_load_articles_from_file(self):
        articles = self.crawler.load_articles_from_file()

        self.assertIs(type(articles), dict)
        self.assertIsNotNone(articles)

    def tearDown(self):
        self.crawler = None
