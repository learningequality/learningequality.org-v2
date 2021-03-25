from django.test import RequestFactory, TestCase
from wagtail_factories import SiteFactory

from learning_equality.utils.context_processors import global_vars
from learning_equality.utils.factories import TrackingFactory


class TrackingTest(TestCase):
    def setUp(self):
        self.site = SiteFactory(site_name="learning_equality", is_default_site=True)
        self.tracking = TrackingFactory(site=self.site)

    def test_context_processor(self):
        request = RequestFactory().get("/")
        request.site = self.tracking.site
        tracking = global_vars(request)
        self.assertEqual(
            tracking, {"GOOGLE_TAG_MANAGER_ID": "GTM-123456", "SEO_NOINDEX": False}
        )
