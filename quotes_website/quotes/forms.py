from typing import Any
from django.forms import ModelForm, CharField, TextInput, Textarea, ModelChoiceField, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Quote, Author, Tag

class QuoteForm(ModelForm):
    quote = CharField(widget=Textarea(attrs={"class": "form-control", "rows": "5"}), required=True)

    author = ModelChoiceField(
        queryset=Author.objects.all().order_by("fullname"),
        empty_label="Choose author",
        required=True
    )

    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all().order_by("tag"),
        widget=CheckboxSelectMultiple(attrs={"size": "12"}))
    
    class Meta:
        model = Quote
        fields = ["quote", "author", "tags"]


class AuthorForm(ModelForm):
    fullname = CharField(
        max_length=50,
        widget=TextInput(attrs={"class": "form-control"}), required=True)
    
    born_date = CharField(
        max_length=50,
        widget=TextInput(attrs={"class": "form-control"}), required=True)
    
    born_location = CharField(
        max_length=150,
        widget=TextInput(attrs={"class": "form-control"}), required=True)
    
    description = CharField(widget=Textarea(attrs={"class": "form-control"}), required=True)

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class TagForm(ModelForm):
    tag = CharField(
        max_length=50,
        widget=TextInput(attrs={"class": "form-control"}), required=True)
    
    class Meta:
        model = Tag
        fields = ["tag",]

class DeleteTagForm(ModelForm):
    tag = CharField(
        max_length=50,
        widget=TextInput(attrs={"class": "form-control"}), required=True)
    
    class Meta:
        model = Tag
        fields = ["tag",]


class DeleteAuthorForm(ModelForm):
    fullname = CharField(
        max_length=50,
        widget=TextInput(attrs={"class": "form-control"}), required=True)
    
    class Meta:
        model = Author
        fields = ["fullname",]
