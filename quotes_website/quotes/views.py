import collections

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuoteForm, AuthorForm, DeleteAuthorForm, TagForm, DeleteTagForm
from .models import Quote, Author, Tag
# Create your views here.

def get_top_10_tags():
    quotes = Quote.objects.all()
    all_tags = []
    for quote in quotes:
        for tag in quote.tags.all():
            all_tags.append(tag.tag)
    tags_count = collections.Counter(all_tags)
    most_tags = tags_count.most_common(10)
    top_10_tags = []
    for tag in most_tags:
        top_10_tags.append(tag[0])
    return top_10_tags

def main(request, page=1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_page = paginator.page(page)
    top_10_tags = get_top_10_tags()
    return render(request, 'quotes/index.html', context={'title': 'Quotes to Scrape', 'quotes': quotes_page,
                                                         'top_10_tags': top_10_tags, 'current_page': page})

def get_author(request, author):
    author_fullname = author.split('-')[-1]
    author = Author.objects.filter(fullname__contains=author_fullname)[0]
    top_10_tags = get_top_10_tags()
    return render(request, 'quotes/get_author.html', context={'title': 'Quotes to Scrape', 'author': author,
                                                              'top_10_tags': top_10_tags})

@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        quote_form = QuoteForm()

    return render(request, "quotes/add_quote.html", {"quote_form": quote_form})

@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        author_form = AuthorForm()

    return render(request, "quotes/add_author.html", {"author_form": author_form})

@login_required
def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        tag_form = TagForm()

    return render(request, "quotes/add_tag.html", {"tag_form": tag_form})

@login_required
def delete_quote(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    quote.delete()
    return redirect(to='quotes:root')

@login_required
def delete_author(request):
    del_author_form = DeleteAuthorForm()
    if request.method == "POST":
        form = DeleteAuthorForm(request.POST)
        if form.is_valid():
            author = Author.objects.filter(fullname=form.cleaned_data['fullname'])[0]
            author.delete()
            return redirect(to="quotes:root")

    return render(request, "quotes/delete_author.html", {"del_author_form": del_author_form})

@login_required
def delete_tag(request):
    delete_tag_form = TagForm()
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = Tag.objects.filter(tag=form.cleaned_data['tag'])[0]
            tag.delete()
            return redirect(to="quotes:root")

    return render(request, "quotes/delete_tag.html", {"delete_tag_form": delete_tag_form})

def get_tag(request, tag, page=1):
    tag_ = Tag.objects.get(tag=tag)
    quotes = Quote.objects.filter(tags=tag_.id)
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_page = paginator.page(page)
    tag_url = f'tag/{tag}/page'
    top_10_tags = get_top_10_tags()
    return render(request, 'quotes/index.html', context={'title': 'Quotes to Scrape', 'quotes': quotes_page, 
                                                         'tag_url': tag_url, 'current_page': page, 'top_10_tags': top_10_tags})