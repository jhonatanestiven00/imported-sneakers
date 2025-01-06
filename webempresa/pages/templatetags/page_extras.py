from django import template
from pages.models import PageDB

register= template.Library()

@register.simple_tag
def get_page_list():
    pages= PageDB.objects.all()
    return pages