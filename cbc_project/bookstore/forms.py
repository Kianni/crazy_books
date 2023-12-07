from django import forms
from .models import Book, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors', 'year_published']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['my_review', 'stars', 'unfinished']
