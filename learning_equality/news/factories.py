import factory
import wagtail_factories
from faker import Factory as FakerFactory

from .models import NewsIndex, NewsPage

faker = FakerFactory.create()


class NewsPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = NewsPage

    title = factory.Faker("text", max_nb_chars=25)
    introduction = factory.Faker("text", max_nb_chars=100)


class NewsIndexPageFactory(wagtail_factories.PageFactory):
    class Meta:
        model = NewsIndex

    title = factory.Faker("text", max_nb_chars=25)
