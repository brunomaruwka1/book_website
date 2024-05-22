from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from .forms import CustomerForm, CreateUserForm
from .models import Book, Opinion
from django.db.models import Avg


# Create your views here.
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() 
    context = {'form':form}
    return render(request, 'hello.html', context)

def createCustomer(request):

    form = CustomerForm()
    if request.method == 'POST':
        print("Printing POST:", request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'hello.html', context)# views.py


def book_rankings(request):
    # Annotate each book with its average rating
    books_with_avg_rating = Book.objects.annotate(avg_rating=Avg('opinion__rating'))
    # Sort books by average rating in descending order
    sorted_books = books_with_avg_rating.order_by('-avg_rating')
    return render(request, 'rankings.html', {'books': list(sorted_books)})

def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    avg_rating = Opinion.objects.filter(book=book).aggregate(Avg('rating'))['rating__avg']
    context = {
        'book': book,
        'avg_rating': avg_rating
    }
    return render(request, 'book.html', context)