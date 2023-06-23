from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
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



# --------SUB CATEGORY--------
@login_required
def sub_category(request):
    context = context_data()
    context['page_title'] = 'Sub Categories'
    return render(request, 'ad/sub_category.html', context)


# --------BOOK--------
@login_required
def book(request):
    context = context_data()
    context['page_title'] = 'Books'
    return render(request, 'ad/book.html', context)