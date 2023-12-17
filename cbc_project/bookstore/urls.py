from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.books, name='books'),
    path('reviews', views.reviews, name='reviews'),
    path('new_book', views.new_book, name='new_book'),
    path('new_review/<int:book_id>/', views.new_review, name='new_review'),
    path('book/<int:book_id>/', views.book, name='book'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
]