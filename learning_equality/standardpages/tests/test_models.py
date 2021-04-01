from wagtail.tests.utils import WagtailPageTests

from learning_equality.home.models import HomePage
from learning_equality.standardpages.factories import (
    IndexPageFactory,
    InformationPageFactory,
)
from learning_equality.standardpages.models import IndexPage, InformationPage


class StandrdPageTests(WagtailPageTests):
    def test_factories(self):
        InformationPageFactory()
        IndexPageFactory()

    def test_can_create_index_page_under_home_page(self):
        self.assertCanCreateAt(HomePage, IndexPage)

    def test_can_create_information_page_under_index_page(self):
        self.assertCanCreateAt(IndexPage, InformationPage)
