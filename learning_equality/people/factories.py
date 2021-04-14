import factory
import wagtail_factories
from faker import Factory as FakerFactory
from faker import Faker
from django.utils.text import slugify
import random

from .models import TeamMemberIndexPage, TeamMemberPage
from .choices import PersonType

faker = FakerFactory.create()


"""
example cli usage:
factories.PersonPageFactory(parent=PersonIndexPage.objects.first())
factories.PersonPageFactory.create_batch(10, parent=PersonIndexPage.objects.first())

you'll want to give the factory-created page a parent, in this case we're assuming a parent page is created already

"""


def get_person_type():
    "Return a random person type from available choices."
    person_type_choices = [x[0] for x in PersonType.choices]
    return random.choice(person_type_choices)


class TeamMemberPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = TeamMemberPage

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    title = factory.LazyAttribute(lambda obj: f"{obj.first_name} {obj.last_name}")
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    job_title = factory.Faker("text", max_nb_chars=25)
    pronouns = "They/them"
    person_type = factory.LazyFunction(get_person_type)
    biography = factory.Faker("text", max_nb_chars=500)
    photo = factory.SubFactory(wagtail_factories.ImageChooserBlockFactory)


class TeamMemberIndexPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = TeamMemberIndexPage

    title = factory.Faker("text", max_nb_chars=25)
