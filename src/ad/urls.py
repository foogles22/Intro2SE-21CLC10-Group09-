from django.urls import path
from . import views

app_name = 'ad'

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('category/', views.category, name = 'category'),
    path('sub_category/', views.sub_category, name = 'sub_category'),
    path('book/', views.book, name = 'book'),
]