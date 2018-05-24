from article import Article
import unittest


class ArticleTest(unittest.TestCase):

    def setUp(self):
        self.article = Article('http://www.test.com', 'Test', 'Monday May 15, 2018', 'Blah blah blah')
        self.article_two = Article('http://www.test2.com', 'Test2', 'Wednesday December 12, 2012', 'Blah blah blah')

    def testDateFormatter(self):
        self.assertEqual('2018-05-15', self.article.date_published)
        self.assertEqual('2012-12-12', self.article_two.date_published)

    def tearDown(self):
        self.article = None
