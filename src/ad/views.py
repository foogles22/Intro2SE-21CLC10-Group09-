from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def context_data():
    context = {
        'page_title': '',
        'system_name': 'Wellib',
    }
    return context


def home(request):
    context = context_data()
    context['page_title'] = 'Admin Home'
    return render(request, 'ad/home.html', context)

def category(request):
    context = context_data()
    context['page_title'] = 'Categories'
    return render(request, 'ad/category.html', context)

def sub_category(request):
    context = context_data()
    context['page_title'] = 'Sub Categories'
    return render(request, 'ad/sub_category.html', context)

def book(request):
    context = context_data()
    context['page_title'] = 'Books'
    return render(request, 'ad/book.html', context)