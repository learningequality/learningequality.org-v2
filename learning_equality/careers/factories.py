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

class CareersPageFactory(wagtail_factories.PageFactory):


    class Meta:
        model = CareersPage

class TestimonialFactory(factory.django.DjangoModelFactory):
    page = factory.SubFactory("learning_equality.careers.factories.BoardPageFactory")
    class Meta:
        model = Testimonial

class PerkFactory(factory.django.DjangoModelFactory):
    page = factory.SubFactory("learning_equality.careers.factories.BoardPageFactory")
    class Meta:
        model = Perk


class CareersPageCarouselImagesFactory(factory.django.DjangoModelFactory):
    page = factory.SubFactory("learning_equality.careers.factories.BoardPageFactory")
    class Meta:
        model = CareersPageCarouselImages
