from django.urls import path
from . import views
from .views import book_rankings

urlpatterns = [
    path('register', views.register),
    path('login', views.register),
    path('rankings/', book_rankings, name='book_rankings'),
    path('books/<int:book_id>/', views.book_details, name='book_details')
]