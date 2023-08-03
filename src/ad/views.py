from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from . import forms
# Create your views here.

def context_data():
    context = {
        'page_title': '',
        'system_name': 'Wellib',
    }
    return context

# AUTHENTICATE-AUTHENTICATE-AUTHENTICATE-AUTHENTICATE-AUTHENTICATE-AUTHENTICATE-AUTHENTICATE-AUTHENTICATE

def login_user(request):
    context = context_data()
    context['page_title'] = 'Login'
    if request.method == "POST":
        auth = authenticate(username = request.POST['userID'], password = request.POST['password'])
        if auth is not None:
            login(request,auth)
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request, 'authenticate/login.html', context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/home/')

def register_user(request):
    context = context_data()
    context['page_title'] = 'Register'
    if request.method == "POST":
        pass
    else:
        return render(request, 'authenticate/register.html', context)


# ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN
# --------HOME--------
@login_required
def home(request):
    context = context_data()
    context['page_title'] = 'Admin Home'
    return render(request, 'ad/home.html', context)

# --------CATEGORY--------
@login_required
def category(request):
    context = context_data()
    context['page_title'] = 'Categories'
    context['category'] = models.Category.objects.all()
    return render(request, 'ad/category.html', context)

@login_required
def manage_category(request, name = None):
    context = context_data()
    context['page_title'] = 'Manage Categories'
    if name:
        context['category'] = models.Category.objects.get(pk = name)
        context['type'] = 'Save'
    else:
        context['category'] = {}
        context['type'] = 'Add'
    return render(request, 'ad/manage_category.html', context)

@login_required
def save_category(request):
    if request.method == "POST":
        post = request.POST
        if post['id']:
            category = models.Category.objects.get(pk = post['id'])
            category = forms.EditCategory(request.POST, instance=category)
        else:
            category = forms.SaveCategory(request.POST)
        if category.is_valid():
            category.save()
            messages.success(request, 'New category added')
        else:
            for field in category.errors.values():
                for error in field:
                    messages.error(request, error)
        return HttpResponseRedirect('/category/')
    else:
        pass

@login_required
def delete_category(request, name):
    category = models.Category.objects.get(pk = name)
    category.delete()
    return HttpResponseRedirect('/category/')

@login_required
def view_category(request, name):
    context = context_data()
    context['page_title'] = 'View Categories'
    context['category'] = models.Category.objects.get(pk = name)
    return render(request, 'ad/view_category.html', context)


# --------SOURCE TYPE--------
@login_required
def source_type(request):
    context = context_data()
    context['page_title'] = 'Source Types'
    context['source_type'] = models.SourceType.objects.all()
    return render(request, 'ad/source_type.html', context)

def manage_source_type(request, code = None):
    context = context_data()
    context['page_title'] = 'Manage Source Type'
    if code:
        context['source_type'] = models.SourceType.objects.get(pk = code)
        context['type'] = 'Save'
    else:
        context['source_type'] = {}
        context['type'] = 'Add'
    return render(request, 'ad/manage_source_type.html', context)

@login_required
def save_source_type(request):
    if request.method == "POST":
        post = request.POST
        if post['id']:
            source_type = models.SourceType.objects.get(pk = post['id'])
            source_type = forms.EditCategory(request.POST, instance=source_type) 
        else:
            source_type = forms.SaveSourceType(request.POST)
        if source_type.is_valid():
            source_type.save()
            messages.success(request, 'New source type added')
        else:
            for field in source_type.errors.values():
                for error in field:
                    messages.error(request, error)
        return HttpResponseRedirect('/source_type/')
    else:
        pass

@login_required
def delete_source_type(request, code):
    source_type = models.SourceType.objects.get(pk = code)
    source_type.delete()
    return HttpResponseRedirect('/source_type/')

@login_required
def view_source_type(request, code):
    context = context_data()
    context['page_title'] = 'View Source Types'
    context['source_type'] = models.SourceType.objects.get(pk = code)
    return render(request, 'ad/view_source_type.html', context)

# --------LANGUAGE------------
@login_required
def language(request):
    context = context_data()
    context['page_title'] = 'Languages'
    context['language'] = models.Language.objects.all()
    return render(request, 'ad/language.html', context)

def manage_language(request, code = None):
    context = context_data()
    context['page_title'] = 'Manage Language'
    if code:
        context['language'] = models.Language.objects.get(pk = code)
        context['type'] = 'Save'
    else:
        context['language'] = {}
        context['type'] = 'Add'
    return render(request, 'ad/manage_language.html', context)

@login_required
def save_language(request):
    if request.method == "POST":
        post = request.POST
        if post['id']:
            language = models.Language.objects.get(pk = post['id'])
            language = forms.EditLanguage(request.POST, instance=language) 
        else:
            language = forms.SaveLanguage(request.POST)
        if language.is_valid():
            language.save()
            messages.success(request, 'New language added')
        else:
            for field in language.errors.values():
                for error in field:
                    messages.error(request, error)
        return HttpResponseRedirect('/language/')
    else:
        pass

@login_required
def delete_language(request, code):
    language = models.Language.objects.get(pk = code)
    language.delete()
    return HttpResponseRedirect('/language/')

@login_required
def view_language(request, code):
    context = context_data()
    context['page_title'] = 'View Languages'
    context['language'] = models.Language.objects.get(pk = code)
    return render(request, 'ad/view_language.html', context)

# --------BOOK--------
@login_required
def book(request):
    context = context_data()
    context['page_title'] = 'Books'
    context['book'] = models.Book.objects.all()
    return render(request, 'ad/book.html', context)

def manage_book(request, title = None):
    context = context_data()
    context['page_title'] = 'Manage Book'
    context['category'] = models.Category.objects.all()
    if title:
        context['book'] = models.Book.objects.get(pk = title)
        context['type'] = 'Save'
    else:
        context['book'] = {}
        context['type'] = 'Add'
    context['category'] = models.Category.objects.all()
    context['sourcetype'] = models.SourceType.objects.all()
    context['language'] = models.Language.objects.all()
    return render(request, 'ad/manage_book.html', context)

@login_required
def save_book(request):
    if request.method == "POST":
        post = request.POST
        if post['id']:
            book = models.Book.objects.get(pk = post['id'])
            book = forms.SaveBook(request.POST, request.FILES, instance=book)
        else:
            book = forms.SaveBook(request.POST, request.FILES)
        if book.is_valid():
            book.save() 
        else:
            print(book.errors.keys(), book.errors.values())
        return HttpResponseRedirect('/book/')
    else:
        pass

@login_required
def delete_book(request, title):
    book = models.Book.objects.get(pk = title)
    book.delete()
    return HttpResponseRedirect('/book/')

@login_required
def view_book(request, title):
    context = context_data()
    context['page_title'] = 'View Books'
    context['book'] = models.Book.objects.get(pk = title)
    return render(request, 'ad/view_book.html', context)

# ---------Borrowing Transaction-----------
@login_required
def borrowing(request):
    context = context_data()
    context['page_title'] = 'Borrowing Transaction'
    return render(request, 'ad/borrowing.html', context)

# ---------------------Users----------------
@login_required
def user(request):
    context = context_data()
    context['page_title'] = 'Users'
    return render(request, 'ad/user.html', context)