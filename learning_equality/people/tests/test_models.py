from wagtail.tests.utils import WagtailPageTests

from learning_equality.home.models import HomePage
from learning_equality.people.factories import (
    PersonIndexPageFactory,
    PersonPageFactory,
)
from learning_equality.people.models import PersonIndexPage, PersonPage


class PeopleTests(WagtailPageTests):
    def test_factories(self):
        PersonPageFactory()
        PersonIndexPageFactory()

    def test_can_create_person_page_under_home_page(self):
        self.assertCanCreateAt(HomePage, PersonIndexPage)

    def test_can_create_person_page_under_person_index_page(self):
        self.assertCanCreateAt(PersonIndexPage, PersonPage)
