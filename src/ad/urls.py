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
    path('home/', views.home, name = 'home'),
    # --------CATEGORY--------
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
    path('manage_user/', views.manage_user, name = 'manage_user'),
    # path('manage_user/<int:id>', views.manage_user, name = 'manage_user_pk'),
    path('save_user/', views.save_user, name = 'save_user'),
    path('delete_user/<int:id>', views.delete_user, name = 'delete_user'),
    # path('view_user/<int:id>', views.view_user, name= 'view_user'),
    path('edit_profile/<int:id>', views.edit_profile, name='edit_profile'),
]