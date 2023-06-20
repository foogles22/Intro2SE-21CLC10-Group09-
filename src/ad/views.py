from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from . import models
from . import forms
# Create your views here.

def context_data():
    context = {
        'page_title': '',
        'system_name': 'Wellib',
    }
    return context

# --------HOME--------
def home(request):
    context = context_data()
    context['page_title'] = 'Admin Home'
    return render(request, 'ad/home.html', context)


# --------CATEGORY--------
def category(request):
    context = context_data()
    context['page_title'] = 'Categories'
    context['data'] = models.Category.objects.all()
    return render(request, 'ad/category.html', context)

def manage_category(request):
    context = context_data()
    context['page_title'] = 'Manage Categories'
    context['category'] = forms.SaveCategory()
    if request.method == "POST":
        category = forms.SaveCategory(request.POST)
        category.save()
        return HttpResponseRedirect('category/')
    else:
        return render(request, 'ad/manage_category.html', context)

# --------SUB CATEGORY--------
def sub_category(request):
    context = context_data()
    context['page_title'] = 'Sub Categories'
    return render(request, 'ad/sub_category.html', context)


# --------BOOK--------
def book(request):
    context = context_data()
    context['page_title'] = 'Books'
    return render(request, 'ad/book.html', context)