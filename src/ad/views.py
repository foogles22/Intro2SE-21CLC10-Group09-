from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
#Comment stupid stuff
#add more comment

# --------CATEGORY--------
@login_required
def category(request):
    context = context_data()
    context['page_title'] = 'Categories'
    context['category'] = models.Category.objects.all()
    return render(request, 'ad/category.html', context)

@login_required
def manage_category(request, id = None):
    context = context_data()
    context['page_title'] = 'Manage Categories'
    if id:
        context['category'] = models.Category.objects.get(pk = id)
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
            category = forms.SaveCategory(request.POST, instance=category) 
        else:
            category = forms.SaveCategory(request.POST)
        category.save()
        return HttpResponseRedirect('/category/')
    else:
        pass

@login_required
def delete_category(request, id):
    category = models.Category.objects.get(pk = id)
    category.delete()
    return HttpResponseRedirect('/category/')

@login_required
def view_category(request, id):
    context = context_data()
    context['page_title'] = 'View Categories'
    context['category'] = models.Category.objects.get(pk = id)
    return render(request, 'ad/view_category.html', context)


# --------SOURCE TYPE--------
@login_required
def source_type(request):
    context = context_data()
    context['page_title'] = 'Source Types'
    return render(request, 'ad/source_type.html', context)

# --------LANGUAGE------------
@login_required
def language(request):
    context = context_data()
    context['page_title'] = 'Language'
    return render(request, 'ad/language.html', context)

# --------BOOK--------
@login_required
def book(request):
    context = context_data()
    context['page_title'] = 'Books'
    return render(request, 'ad/book.html', context)

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