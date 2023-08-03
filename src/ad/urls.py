from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),    
    # ----------------------------------ADMIN------------------------------------------------
    # --------CATEGORY--------
    path('home/', views.home, name = 'home'),
    path('category/', views.category, name = 'category'),
    path('manage_category/', views.manage_category, name = 'manage_category'),
    path('manage_category/<str:name>', views.manage_category, name = 'manage_category_pk'),
    path('save_category/', views.save_category, name = 'save_category'),
    path('delete_category/<str:name>', views.delete_category, name = 'delete_category'),
    path('view_category/<str:name>', views.view_category, name= 'view_category'),

    # --------Source Type--------
    path('source_type/', views.source_type, name = 'source_type'),
    path('manage_source_type/', views.manage_source_type, name = 'manage_source_type'),
    path('manage_source_type/<str:code>', views.manage_source_type, name = 'manage_source_type_pk'),
    path('save_source_type/', views.save_source_type, name = 'save_source_type'),
    path('delete_source_type/<str:code>', views.delete_source_type, name = 'delete_source_type'),
    path('view_source_type/<str:code>', views.view_source_type, name= 'view_source_type'),    
    
    # --------Languages----------
    path('language/', views.language, name = 'language'),
    path('manage_language/', views.manage_language, name = 'manage_language'),
    path('manage_language/<str:code>', views.manage_language, name = 'manage_language_pk'),
    path('save_language/', views.save_language, name = 'save_language'),
    path('delete_language/<str:code>', views.delete_language, name = 'delete_language'),
    path('view_language/<str:code>', views.view_language, name= 'view_language'), 

    # --------Book--------
    path('book/', views.book, name = 'book'),
    path('manage_book/', views.manage_book, name = 'manage_book'),
    path('manage_book/<str:title>', views.manage_book, name = 'manage_book_pk'),
    path('save_book/', views.save_book, name = 'save_book'),
    path('delete_book/<str:title>', views.delete_book, name = 'delete_book'),
    path('view_book/<str:title>', views.view_book, name= 'view_book'), 

    # --------Borrowing Transactions-------
    path('borrowing/', views.borrowing, name = 'borrowing'),

    # --------------User------------------
    path('user/', views.user, name = 'user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
