import unittest
from typing import Dict
import zencrawler
from article import Article


class ZenCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.crawler = zencrawler

    def testWriteArticlesToFile(self):
        article_one = Article('http://www.test.com', 'Test', 'Monday May 15, 2018', 'Blah blah blah')
        article_two = Article('http://www.test2.com', 'Test2', 'Monday June 1, 2012', 'Sample content')

        articles: Dict[str, Article] = {
            'http://www.test.com': article_one,
            'http://www.test2.com': article_two
        }
        self.assertTrue(self.crawler.writeArticlesToFile(articles))

    def testLoadArticlesFromFile(self):
        articles = self.crawler.loadArticlesFromFile()
        self.assertIsNotNone(articles)

    def tearDown(self):
        self.crawler = None
