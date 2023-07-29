from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . import models
from . import forms
from .decorators import user_is_authenticated, allowed_users
from datetime import timedelta
from django.core.paginator import Paginator

# Create your views here.


def context_data():
    context = {
        "page_title": "",
        "system_name": "Wellib",
    }
    return context


# AUTHENTICATE-AUTHENTICATE-AUTHENTICATE-AUTHENTICATE-AUTHENTICATE-AUTHENTICATE-AUTHENTICATE-AUTHENTICATE


@user_is_authenticated
def login_user(request):
    context = context_data()
    context["page_title"] = "Login"
    if request.method == "POST":
        auth = authenticate(
            username=request.POST["userID"], password=request.POST["password"]
        )
        if auth is not None:
            login(request, auth)
            if request.user.profile.first_time == True:
                messages.info(request, 'Please edit your profile!')
                return redirect('edit_profile', request.user.id)
            else:
                messages.success(request, 'You have logged in!')
                return redirect('home')        
        else:
            messages.error(request, 'Login failed!')
            return render(request, "authenticate/login.html", context)        
    return render(request, "authenticate/login.html", context)


def logout_user(request):
    logout(request)
    return redirect("login")

@user_is_authenticated
def register_user(request, *args, **kwargs):
    context = context_data()
    context["page_title"] = "Register"
    register_form = forms.CustomUserCreationForm()
    if request.method == "POST":
        register_form = forms.CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    context["register_form"] = register_form
    return render(request, "authenticate/register.html", context)

# ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN
# --------HOME--------
@login_required
@allowed_users(allowed_roles=['ADMIN','LIBRARIAN'])
def home(request):
    context = context_data()
    context["page_title"] = "Admin Home"
    return render(request, "ad/home.html", context)


# --------CATEGORY--------
@login_required
@allowed_users(allowed_roles=['ADMIN'])
def category(request):
    context = context_data()
    context["page_title"] = "Categories"
    context["category"] = models.Category.objects.all()
    return render(request, "ad/category.html", context)


@login_required
@allowed_users(allowed_roles=['ADMIN'])
def manage_category(request, id=None):
    context = context_data()
    context["page_title"] = "Manage Categories"
    if id:
        context["category"] = models.Category.objects.get(pk=id)
        context["type"] = "Save"
    else:
        context["category"] = {}
        context["type"] = "Add"
    return render(request, "ad/manage_category.html", context)


@login_required
@allowed_users(allowed_roles=['ADMIN'])
def save_category(request):
    if request.method == "POST":
        post = request.POST
        if post["id"]:
            category = models.Category.objects.get(pk=post["id"])
            category = forms.SaveCategory(post, instance=category)
        else:
            category = forms.SaveCategory(post)
        category.save()
        return redirect("category")
    else:
        pass


@login_required
@allowed_users(allowed_roles=['ADMIN'])
def delete_category(request, id):
    category = models.Category.objects.get(pk=id)
    category.delete()
    return redirect("category")


@login_required
@allowed_users(allowed_roles=['ADMIN'])
def view_category(request, id):
    context = context_data()
    context["page_title"] = "View Categories"
    context["category"] = models.Category.objects.get(pk=id)
    return render(request, "ad/view_category.html", context)


# --------SOURCE TYPE--------
@login_required
@allowed_users(allowed_roles=['ADMIN'])
def source_type(request):
    context = context_data()
    context["page_title"] = "Source Types"
    return render(request, "ad/source_type.html", context)


# --------LANGUAGE------------
@login_required
@allowed_users(allowed_roles=['ADMIN'])
def language(request):
    context = context_data()
    context["page_title"] = "Language"
    return render(request, "ad/language.html", context)


# --------BOOK--------
@login_required
@allowed_users(allowed_roles=['ADMIN'])
def book(request):
    context = context_data()
    context["page_title"] = "Books"
    return render(request, "ad/book.html", context)


# Librarian-Librarian-Librarian-Librarian-Librarian-Librarian-Librarian-Librarian-Librarian-Librarian

# ---------LOAN Transaction-----------
@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def loan(request):
    context = context_data()
    context["page_title"] = "Loan Transaction"
    loans = models.LoanTransaction.objects.all()

    # setup pagination
    p = Paginator(loans, 2)
    page = request.GET.get('page')
    loan_p = p.get_page(page)
    context["loan"] = loan_p
    return render(request, "ad/loan.html", context)

@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def manage_loan(request, id=None):
    context = context_data()
    context["page_title"] = "Manage Loan Transaction"
    if id:
        context["loan"] = models.LoanTransaction.objects.get(pk=id)
        context["type"] = "Save"
    else:
        context["loan"] = {}
        context["type"] = "Add"
    return render(request, "ad/manage_loan.html", context)

@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def save_loan(request):
    if request.method == "POST":
        post = request.POST
        if post["id"]:
            loan = models.LoanTransaction.objects.get(pk=post["id"])
            profile = models.Profile.objects.get(identity = post['identity'])
            user = User.objects.get(pk = profile.id)
            book = models.Book.objects.get(pk = post['book'])
            loan.user = user
            loan.book = book
            loan.save(update_fields=['user','book'])
        else:
            profile = models.Profile.objects.get(identity = post['identity'])
            user = User.objects.get(pk = profile.id)
            book = models.Book.objects.get(pk = post['book'])
            loan = models.LoanTransaction(user=user, book=book)
        loan.save()
        return redirect("loan")
    else:
        return redirect("loan")

@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def delete_loan(request, id):
    loan = models.LoanTransaction.objects.get(pk=id)
    loan.delete()
    return redirect("loan")


@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def return_book(request, id):
    loan = models.LoanTransaction.objects.get(pk=id)
    loan.returned = True
    loan.save(update_fields=['returned'])
    return redirect("loan")

@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def renew_book(request, id):
    loan = models.LoanTransaction.objects.get(pk=id)
    loan.date_expired += timedelta(7)
    loan.save(update_fields=['date_expired'])
    return redirect("loan")



# ---------------------Users----------------
@login_required
@allowed_users(allowed_roles=['ADMIN'])
def user(request):
    context = context_data()
    context["page_title"] = "Users"
    context["users"] = User.objects.all()
    return render(request, "ad/user.html", context)

@login_required
@allowed_users(allowed_roles=['ADMIN'])
def manage_user(request):
    context = context_data()
    context["page_title"] = "Manage Users"
    context["user"] = {}
    context["type"] = "Add"
    return render(request, "ad/manage_user.html", context)
    
def save_profile(profile, post):
    profile.role = post['role']
    profile.first_name = post['first_name'] 
    profile.last_name = post['last_name']
    profile.email = post['email']
    profile.first_time = False
    profile.save(update_fields = ['role','first_name','last_name','email','first_time'])
    profile.init_identity()
    profile.save()

@login_required
@allowed_users(allowed_roles=['ADMIN'])
def save_user(request):
    if request.method == "POST":
        post = request.POST
        user = User.objects.create_user(username = post['username'], password = post['password'])
        user.save()
        profile = models.Profile.objects.get(pk = user.id)
        save_profile(profile,post)
        return redirect("user")
    else:
        pass


@login_required
def edit_profile(request, id):
    context = context_data()
    context["page_title"] = "Edit Profile"
    if request.method == "POST":
        profile = models.Profile.objects.get(pk = id)
        profile.first_time = False
        profile.save()
        profile = forms.EditProfile(request.POST, instance = profile)
        if profile.is_valid():
            profile.save()
            return redirect('home')
    context["profile"] = models.Profile.objects.get(pk = id)
    return render(request, 'ad/edit_profile.html', context)


@login_required
@allowed_users(allowed_roles=['ADMIN'])
def delete_user(request, id):
    user = User.objects.get(pk = id)
    user.delete()
    return redirect("user")


# @login_required
# def view_user(request, id):
#     context = context_data()
#     context["page_title"] = "View Categories"
#     context["user"] = models.user.objects.get(pk=id)
#     return render(request, "ad/view_user.html", context)


# SEARCHING

def identity_search(request):
    if request.method == "GET" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        search_query = request.GET.get('query', '')
        items = models.Profile.objects.filter(identity__contains=search_query)[:10]
        item_list = [item.identity for item in items]
        return JsonResponse(item_list, safe=False)
    return render(request, 'manage_loan.html')

def book_search(request):
    if request.method == "GET" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        search_query = request.GET.get('query', '')
        items = models.Book.objects.filter(pk__contains=search_query)[:10]
        item_list = [item.pk for item in items]
        return JsonResponse(item_list, safe=False)
    return render(request, 'manage_loan.html')