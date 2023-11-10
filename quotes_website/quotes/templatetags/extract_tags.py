from django import template

register = template.Library()


def tags(quote_tags):
    return ', '.join([tag.tag for tag in quote_tags])


register.filter('tags', tags)
