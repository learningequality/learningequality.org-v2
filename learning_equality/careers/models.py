from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Orderable
from wagtail.core.fields import StreamField, RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from learning_equality.utils.models import BasePage


# Create your models here.

"""
Careers has a landing page with work info, and a list of open positions
Header,
summary
'view open positions' maybe as an anchor link to the listings below?
Full width image
Testimonials section
4 blocks (orderable or streamfield?)
ImageCarosuel
Perks
orderable of perks, each with an image, heading, description
Open positions
not sure about this yet, how to link from Greenhouse or what?
"""


class CareersPage(BasePage):
    template = "patterns/pages/careers/careers_page.html"
    introduction = RichTextField(blank=True)
    # full-width image on the page
    photo = models.ForeignKey(
        "images.CustomImage",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    testimonial_section_header = models.CharField(
        blank=True, default="Why work with us?", max_length=255
    )
    perks_section_header = models.CharField(
        blank=True, default="Perks of working with us", max_length=255
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("introduction"),
        MultiFieldPanel(
            [
                FieldPanel("testimonial_section_header"),
                InlinePanel("testimonials", label="Why work with us?"),
            ],
            heading="Testimonials",
        ),
        MultiFieldPanel(
            [
                FieldPanel("perks_section_header"),
                InlinePanel("perks", label="perks"),
            ],
            heading="Perks",
        ),
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5, min_num=1, label="Image")],
            heading="Carousel Images",
        ),
    ]


class Testimonial(Orderable):
    page = ParentalKey(CareersPage, related_name="testimonials")
    quote = models.TextField(
        blank=True,
    )

    author = models.ForeignKey(
        "wagtailcore.Page", blank=True, null=True, on_delete=models.SET_NULL
    )
    panels = [
        FieldPanel("quote"),
        PageChooserPanel("author", "people.TeamMemberPage"),
    ]


class Perk(Orderable):
    page = ParentalKey(CareersPage, related_name="perks")
    image = models.ForeignKey(
        "images.CustomImage",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    title = models.CharField(max_length=255)
    description = models.TextField()


class CareersPageCarouselImages(Orderable):

    page = ParentalKey(CareersPage, related_name="carousel_images")
    image = models.ForeignKey(
        "images.CustomImage",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [ImageChooserPanel("image")]
