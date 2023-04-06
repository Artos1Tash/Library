from django.urls import path
from .views import BookListView, index, BookDetailView, AuthorListView, AuthorDetailView, LoanedBooksByUserListView
from django.urls import re_path


urlpatterns = [
    path('', index, name='index'),
    re_path(r'^$', index, name='index'),

    path('books/', BookListView.as_view(), name='books'),
    re_path(r'^books/$', BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', BookDetailView.as_view(), name='book-detail'),

    path('authors/', AuthorListView.as_view(), name='authors'),
    re_path(r'^author/$', AuthorListView.as_view(), name='authors'),
    re_path(r'^author/(?P<pk>\d+)', AuthorDetailView.as_view(), name='author-detail'),

    re_path(r'^mybooks/$', LoanedBooksByUserListView.as_view(), name='my-borrowed'),

]
