from django.urls import path
from . import views

app_name = 'ad'

urlpatterns = [
    # --------HOME--------
    path('home/', views.home, name = 'home'),


    # --------CATEGORY--------
    path('category/', views.category, name = 'category'),
    path('manage_category', views.manage_category, name = 'manage_category'),

    # --------SUB CATEGORY--------
    path('sub_category/', views.sub_category, name = 'sub_category'),


    # --------BOOK--------
    path('book/', views.book, name = 'book'),

]