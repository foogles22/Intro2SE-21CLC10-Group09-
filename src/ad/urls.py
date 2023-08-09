from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('change_password/', views.change_password, name='change_password'),
    # ----------------------------------READER------------------------------------------------
    path('homepage/', views.homepage, name = 'homepage'), 
    path('searchbook/<int:cate>', views.searchbook, name = 'searchbook'), 
    path('events/', views.events, name = 'events'), 
    path('about/', views.about, name = 'about'), 
    path('help/', views.help, name = 'help'), 
    path('profile/<int:id>', views.profile, name = 'profile'), 
    path('edit_profile/<int:id>', views.edit_profile, name = 'edit_profile'), 
    path('edit_avatar/<int:id>', views.edit_avatar, name = 'edit_avatar'), 
    path('bookdetail/<int:id>', views.bookdetail, name = 'bookdetail'), 
    path('save_comment/<int:id>', views.save_comment, name='save_comment'),



    # ----------------------------------LIBRARIAN--------------------------------------------
    # --------Borrowing Transactions-------
    path('loan/', views.loan, name = 'loan'),
    path('manage_loan/', views.manage_loan, name = 'manage_loan'),
    path('manage_loan/<int:id>', views.manage_loan, name = 'manage_loan_pk'),
    path('save_loan/', views.save_loan, name = 'save_loan'),
    path('delete_loan/<int:id>', views.delete_loan, name = 'delete_loan'),
    path('identity_search/', views.identity_search, name ='identity_search'),
    path('book_search/', views.book_search, name ='book_search'),
    path('return_book/<int:id>', views.return_book, name ='return_book'),
    path('renew_book/<int:id>', views.renew_book, name ='renew_book'),
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

    # --------------User------------------
    path('user/', views.user, name = 'user'),
    path('manage_user/', views.manage_user, name = 'manage_user'),
    # path('manage_user/<int:id>', views.manage_user, name = 'manage_user_pk'),
    path('save_user/', views.save_user, name = 'save_user'),
    path('delete_user/<int:id>', views.delete_user, name = 'delete_user'),
    # path('view_user/<int:id>', views.view_user, name= 'view_user'),
]
