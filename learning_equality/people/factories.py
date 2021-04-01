import factory
import wagtail_factories
from faker import Factory as FakerFactory
from faker import Faker

from .models import PersonIndexPage, PersonPage

faker = FakerFactory.create()


name = Faker().name()


class PersonPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = PersonPage

    first_name = name.split(" ")[0]
    last_name = " ".join(name.split(" ")[1:])
    job_title = factory.Faker("text", max_nb_chars=25)


class PersonIndexPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = PersonIndexPage

    title = factory.Faker("text", max_nb_chars=25)
