from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import BookForm, ReviewForm
from .models import Book, Review


def home(request):
    return render(request, 'bookstore/home.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'bookstore/books.html', {'books': books})

def book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        book = None
    return render(request, 'bookstore/book.html', {'book': book})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'bookstore/reviews.html', {'reviews': reviews})

def new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another view
            return redirect('books')
    else:
        form = BookForm()

    return render(request, 'bookstore/new_book.html', {'form': form})

def new_review(request, book_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # Create the review instance without associating it with a specific book
            review = form.save(commit=False)

            # You can now use the 'book_id' value to associate the review with a specific book
            review.book_id = book_id
            review.save()
            # Redirect to the book's detail page after adding the review
            redirect_url = reverse('book', kwargs={'book_id': book_id})
            return HttpResponseRedirect(redirect_url)
    else:
        form = ReviewForm()

    return render(request, 'bookstore/new_review.html', {'form': form})

def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('reviews')  # Redirect to a suitable URL after editing

    else:
        form = ReviewForm(instance=review)

    return render(request, 'bookstore/edit_review.html', {'form': form, 'review': review})