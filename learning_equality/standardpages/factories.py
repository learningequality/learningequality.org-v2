import factory
import factory.fuzzy
import wagtail_factories
from faker import Factory as FakerFactory

from .models import IndexPage, InformationPage

faker = FakerFactory.create()


class InformationPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = InformationPage

    title = factory.Faker("text", max_nb_chars=25)


class IndexPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = IndexPage

    title = factory.Faker("text", max_nb_chars=25)
