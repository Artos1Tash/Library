from django.http import Http404
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.all().count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_genres': num_genres,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)


class BookListView(ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.all()
    template_name = 'book_list.html'
    paginate_by = 10


# noinspection PyMethodParameters
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

    def book_detail_view(request, pk):
        try:
            book_id = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

        return render(
            request,
            'book_detail.html',
            context={'book': book_id, }
        )


class AuthorListView(ListView):
    context_object_name = 'author_list'
    queryset = Author.objects.all()
    template_name = 'author_list.html'
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'

    def author_detail_view(request, pk):
        try:
            author_id = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404('Author does not exist')

        return render(
            request,
            'author_detail.html',
            context={'author': author_id}
        )
