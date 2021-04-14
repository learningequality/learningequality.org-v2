import factory
import factory.fuzzy
import wagtail_factories
from faker import Factory as FakerFactory
from django.utils.text import slugify


from learning_equality.home.models import HomePage
from .models import TeamMemberIndexPage, TeamMemberPage, BoardMember, BoardPage
from .choices import PersonType, BoardPersonType

faker = FakerFactory.create()


"""
See generate() for example usage
"""


class TeamMemberPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = TeamMemberPage

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    title = factory.LazyAttribute(lambda obj: f"{obj.first_name} {obj.last_name}")
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    job_title = factory.Faker("text", max_nb_chars=25)
    pronouns = "They/them"
    person_type = factory.fuzzy.FuzzyChoice(PersonType.values)
    biography = factory.Faker("text", max_nb_chars=500)
    photo = factory.SubFactory(wagtail_factories.ImageChooserBlockFactory)


class TeamMemberIndexPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = TeamMemberIndexPage

    title = factory.Faker("text", max_nb_chars=25)

    @factory.post_generation
    def add_team_members(self, create, extracted, **kwargs):
        if create:
            TeamMemberPageFactory.create_batch(size=25, parent=self)


class BoardPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = BoardPage

    @factory.post_generation
    def add_board_members(self, create, extracted, **kwargs):
        if create:
            BoardMemberFactory.create_batch(size=12, page=self)


class BoardMemberFactory(factory.django.DjangoModelFactory):
    page = factory.SubFactory("learning_equality.people.factories.BoardPageFactory")
    title = factory.Faker("name")
    biography = factory.Faker("text", max_nb_chars=500)
    person_type = factory.fuzzy.FuzzyChoice(BoardPersonType.values)
    photo = factory.SubFactory(wagtail_factories.ImageChooserBlockFactory)

    class Meta:
        model = BoardMember


def generate():
    home_page = HomePage.objects.first()
    BoardPageFactory(title="Our Board", parent=home_page)
    TeamMemberIndexPageFactory(title="Our Team", parent=home_page)
