from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from learning_equality.news.models import NewsType
from learning_equality.people.models import PersonType

class NewsTypeModelAdmin(ModelAdmin):
    model = NewsType
    menu_icon = "tag"


class PersonTypeModelAdmin(ModelAdmin):
    model = PersonType
    menu_icon = "tag"


class TaxonomiesModelAdminGroup(ModelAdminGroup):
    menu_label = "Taxonomies"
    items = (
        NewsTypeModelAdmin,
        # feature:use_events_app
        PersonTypeModelAdmin,
    )
    menu_icon = "tag"


modeladmin_register(TaxonomiesModelAdminGroup)
