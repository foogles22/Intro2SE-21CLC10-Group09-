from django.urls import path
from . import views
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
    path('manage_category/<int:id>', views.manage_category, name = 'manage_category_pk'),
    path('save_category/', views.save_category, name = 'save_category'),
    path('delete_category/<int:id>', views.delete_category, name = 'delete_category'),
    path('view_category/<int:id>', views.view_category, name= 'view_category'),

    # --------Source Type--------
    path('source_type/', views.source_type, name = 'source_type'),
    path('manage_source_type/', views.manage_source_type, name = 'manage_source_type'),
    path('manage_source_type/<int:id>', views.manage_source_type, name = 'manage_source_type_pk'),
    path('save_source_type/', views.save_source_type, name = 'save_source_type'),
    path('delete_source_type/<int:id>', views.delete_source_type, name = 'delete_source_type'),
    path('view_source_type/<int:id>', views.view_source_type, name= 'view_source_type'),    
    
    # --------Languages----------
    path('language/', views.language, name = 'language'),
    path('manage_language/', views.manage_language, name = 'manage_language'),
    path('manage_language/<int:id>', views.manage_language, name = 'manage_language_pk'),
    path('save_language/', views.save_language, name = 'save_language'),
    path('delete_language/<int:id>', views.delete_language, name = 'delete_language'),
    path('view_language/<int:id>', views.view_language, name= 'view_language'), 

    # --------Book--------
    path('book/', views.book, name = 'book'),
    path('manage_book/', views.manage_book, name = 'manage_book'),
    path('manage_book/<int:id>', views.manage_book, name = 'manage_book_pk'),
    path('save_book/', views.save_book, name = 'save_book'),
    path('delete_book/<int:id>', views.delete_book, name = 'delete_book'),
    path('view_book/<int:id>', views.view_book, name= 'view_book'), 

    # --------Borrowing Transactions-------
    path('borrowing/', views.borrowing, name = 'borrowing'),

    # --------------User------------------
    path('user/', views.user, name = 'user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
