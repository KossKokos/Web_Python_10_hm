
from django import template

# from utils.get_quotes_authors import db
from quotes.models import Author
register = template.Library()

def fullname(fullname):  # authors = db.authors.find()
    author_fullname = fullname.replace('. ', '-').replace(' ', '-').replace('.', '-')
    author_fullname = author_fullname[:-1] if author_fullname[-1] == '-' else author_fullname
    return author_fullname

register.filter('fullname', fullname)