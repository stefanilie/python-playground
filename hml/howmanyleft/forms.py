from django.forms import (
    Form, CharField, Textarea, PasswordInput, ChoiceField, DateField,
    ImageField, EmailField,
)

class SearchForm(Form):
    search_term = CharField(max_length=50)
