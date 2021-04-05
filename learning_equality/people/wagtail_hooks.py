from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.core import hooks


@hooks.register("insert_editor_js")
def editor_js():
    return format_html(
        '<script src="{}"></script>', static("/people/admin/js/update_person_title.js")
    )
