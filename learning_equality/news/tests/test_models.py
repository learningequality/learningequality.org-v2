from wagtail.tests.utils import WagtailPageTests

from learning_equality.home.models import HomePage
from learning_equality.news.factories import NewsIndexPageFactory, NewsPageFactory
from learning_equality.news.models import NewsIndex, NewsPage


class NewsTests(WagtailPageTests):
    def test_factories(self):
        NewsPageFactory()
        NewsIndexPageFactory()

    def test_can_create_news_page_under_home_page(self):
        self.assertCanCreateAt(HomePage, NewsIndex)

    def test_can_create_news_page_under_news_index_page(self):
        self.assertCanCreateAt(NewsIndex, NewsPage)
