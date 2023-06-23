from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [

    path('login/', TemplateView.as_view(template_name = 'authenticate/login.html')),
    path('register/', TemplateView.as_view(template_name = 'authenticate/register.html')),
    
    # ----------------------------------READER------------------------------------------------
    # path('homepage/', views.homepage, name = 'homepage'), 


    # ----------------------------------ADMIN------------------------------------------------
    # --------CATEGORY--------
    path('home/', views.home, name = 'home'),
    path('category/', views.category, name = 'category'),
    path('manage_category/', views.manage_category, name = 'manage_category'),
    path('manage_category/<int:id>', views.manage_category, name = 'manage_category_pk'),
    path('save_category/', views.save_category, name = 'save_category'),
    path('delete_category/<int:id>', views.delete_category, name = 'delete_category'),
    path('view_category/<int:id>', views.view_category, name= 'view_category'),

    # --------SUB CATEGORY--------
    path('sub_category/', views.sub_category, name = 'sub_category'),


    # --------BOOK--------
    path('book/', views.book, name = 'book'),

]