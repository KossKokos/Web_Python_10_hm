from django import template

register = template.Library()


def tags_id(quote_tags):
    return ', '.join([tag.tag for tag in quote_tags])


register.filter('tags_id', tags_id)
