from wagtail.tests.utils import WagtailPageTests

from learning_equality.home.models import HomePage
from learning_equality.people.factories import (
    TeamMemberIndexPageFactory,
    TeamMemberPageFactory,
)
from learning_equality.people.models import TeamMemberIndexPage, TeamMemberPage


class PeopleTests(WagtailPageTests):
    def test_factories(self):
        TeamMemberPageFactory()
        TeamMemberIndexPageFactory()

    def test_can_create_person_page_under_home_page(self):
        self.assertCanCreateAt(HomePage, TeamMemberIndexPage)

    def test_can_create_person_page_under_person_index_page(self):
        self.assertCanCreateAt(TeamMemberIndexPage, TeamMemberPage)
