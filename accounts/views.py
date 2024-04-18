from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerForm, CreateUserForm


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
    return render(request, 'hello.html', context)