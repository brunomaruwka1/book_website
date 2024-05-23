from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404
from .forms import CustomerForm, CreateUserForm
from .models import Book, Opinion, Customer
from django.db.models import Avg
from .forms import CustomerSignUpForm

# Create your views here.
# def register(request):
#     form = CreateUserForm()

#     if request.method == "POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save() 
#     context = {'form':form}
#     return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            customer = form.save()
            login(request, customer)
            return redirect('index')  # Zmień 'index' na nazwę swojego widoku głównego
    else:
        form = CustomerSignUpForm()
    return render(request, 'index.html', {'form': form})

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


def search_books(request):
    query = request.GET.get('query')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = []
    return render(request, 'index.html', {'books': books})
