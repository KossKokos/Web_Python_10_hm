import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes_website.settings')
django.setup()
from quotes.models import Author, Tag, Quote
from .get_quotes_authors import db



def migrate_tables():
    quotes = list(Quote.objects.all())
    for q in quotes:
        print(q)
    authors = db.authors.find()
    for aut in authors:
        author = Author.objects.get_or_create(
            fullname=aut['fullname'],
            born_date=aut['born_date'], 
            born_location=aut['born_location'],
            description=aut['description']
        )

    def get_tags(tags: list):
        tags_ = []
        for tg in tags:
            tag, _ = Tag.objects.get_or_create(tag=tg)
            tags_.append(tag)
        return tags_

    quotes = db.qoutes.find()

    for quot in quotes:
        tags = get_tags(quot['tags'])
        exist_quote = bool(list(Quote.objects.filter(quote=quot['qoute'])))
        if not exist_quote:
            aut = db.authors.find_one({'_id': quot['author']})
            author = Author.objects.get(fullname=aut['fullname'])
            quote = Quote.objects.create(quote=quot['qoute'], author=author)
            for tag in tags:
                quote.tags.add(tag)


if __name__ == '__main__':
    migrate_tables()