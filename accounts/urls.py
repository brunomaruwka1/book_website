from django.urls import path
from . import views
from .views import book_rankings, search_books

urlpatterns = [
    path('register', views.signup),
    path('login', views.signup),
    path('rankings/', book_rankings, name='book_rankings'),
    path('books/<int:book_id>/', views.book_details, name='book_details'),
    path('search/', search_books, name='search_results')
    ]