from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    # ----------------------------------READER------------------------------------------------
    # path('homepage/', views.homepage, name = 'homepage'), 

    # ----------------------------------LIBRARIAN--------------------------------------------

    
    # ----------------------------------ADMIN------------------------------------------------
    # --------CATEGORY--------
    path('home/', views.home, name = 'home'),
    path('category/', views.category, name = 'category'),
    path('manage_category/', views.manage_category, name = 'manage_category'),
    path('manage_category/<int:id>', views.manage_category, name = 'manage_category_pk'),
    path('save_category/', views.save_category, name = 'save_category'),
    path('delete_category/<int:id>', views.delete_category, name = 'delete_category'),
    path('view_category/<int:id>', views.view_category, name= 'view_category'),

    # --------Source Type--------
    path('source_type/', views.source_type, name = 'source_type'),

    # --------Languages----------
    path('language/', views.language, name = 'language'),


    # --------Book--------
    path('book/', views.book, name = 'book'),

    # --------Borrowing Transactions-------
    path('borrowing/', views.borrowing, name = 'borrowing'),

    # --------------User------------------
    path('user/', views.user, name = 'user'),
]