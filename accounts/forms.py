from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1',
                  'password2']

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=True)
    phone = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['email','name', 'last_name', 'phone']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            customer = Customer.objects.create(
                
                name=self.cleaned_data['name'],
                last_name=self.cleaned_data['last_name'],
                phone=self.cleaned_data['phone'],
                email=self.cleaned_data['email']
            )
        return user