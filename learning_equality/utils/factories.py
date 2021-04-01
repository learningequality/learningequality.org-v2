from factory.django import DjangoModelFactory
from faker import Factory as FakerFactory

from .models import Tracking

faker = FakerFactory.create()


class TrackingFactory(DjangoModelFactory):
    class Meta:
        model = Tracking

    google_tag_manager_id = "GTM-123456"
