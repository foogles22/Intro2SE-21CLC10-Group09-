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
from django.utils import timezone
import os
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm

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
                if request.user.profile.role == "ADMIN":
                    return redirect('adhome')
                if request.user.profile.role == "LIBRARIAN":
                    return redirect('libhome')
                if request.user.profile.role == "READER":
                    return redirect('homepage')             
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
    if request.method == "POST":
        register_form = forms.CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Register successfully!')
            return redirect('login')
        else:
            for error in register_form.errors.values():
                messages.error(request, error)
    return render(request, "authenticate/register.html", context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Change password successfully')
        else:
            for field in form.errors.values():
                for error in field:
                    messages.error(request, error)
    return redirect('edit_profile', request.user.id)

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
            messages.success(request, 'Edited profile successfully')
        else:
            for field in profile.errors.values():
                for error in field:
                    messages.error(request, error)
    context["profile"] = models.Profile.objects.get(pk = id)
    return render(request, 'homepage/edit_profile.html', context)

@login_required
def edit_avatar(request, id):
    context = context_data()
    if request.method == "POST":
        profile = models.Profile.objects.get(pk = id)
        profile = forms.EditAvatar(request.POST, request.FILES, instance = profile)
        if profile.is_valid():
            profile.save()
            messages.success(request, "Edit avatar successfully")
        else:
            messages.error(request, "Can not change your avatar")
    
    context["profile"] = models.Profile.objects.get(pk = id)
    return render(request, 'homepage/edit_profile.html', context)

@login_required
@allowed_users(allowed_roles=['ADMIN'])
def delete_user(request, id):
    user = User.objects.get(pk = id)
    messages.success(request, 'Deleting acount succeed')
    user.delete()
    return redirect("user", 'id')

# ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN
# --------HOME--------
@login_required
@allowed_users(allowed_roles=['ADMIN'])
def adhome(request):
    context = context_data()
    context["page_title"] = "Admin Home"
    return render(request, "ad/adhome.html", context)

# --------CATEGORY--------
@login_required
def category(request, order = 'id'):
    context = context_data()
    context['page_title'] = 'Categories'
    category = models.Category.objects.all().order_by(order)
    p = Paginator(category, 3)
    page = request.GET.get('page')
    category = p.get_page(page)
    context["category"] = category
    return render(request, 'ad/category.html', context)

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
        if post['id']:
            category = models.Category.objects.get(pk = post['id'])
            category = forms.SaveCategory(request.POST,request.FILES, instance=category)
        else:
            category = forms.SaveCategory(request.POST,request.FILES)
        if category.is_valid():
            category.save()
            if post['id']:
                messages.success(request, 'Category edited successfully')
                return redirect('category', 'id')
            else:
                messages.success(request, 'New category added')
        else:
            print(category.errors.as_text)
            for field in category.errors.values():
                for error in field:
                    messages.error(request, error)
    else:
        messages.error(request, 'No data has been sent')
    return HttpResponseRedirect('/manage_category/')
    

@login_required
def delete_category(request, id):
    category = models.Category.objects.get(pk = id)
    if len(category.image) > 0:
        os.remove(category.image.path)
    category.delete()
    messages.success(request,'Delete category successfully')
    return HttpResponseRedirect('/category/id')

# --------SOURCE TYPE--------
@login_required
def source_type(request, order = 'id'):
    context = context_data()
    context['page_title'] = 'Source Types'
    source_type = models.SourceType.objects.all().order_by(order)
    p = Paginator(source_type, 3)
    page = request.GET.get('page')
    source_type = p.get_page(page)
    context["source_type"] = source_type
    return render(request, 'ad/source_type.html', context)

def manage_source_type(request, id = None):
    context = context_data()
    context['page_title'] = 'Manage Source Type'
    if id:
        context['source_type'] = models.SourceType.objects.get(pk = id)
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
            source_type = forms.SaveSourceType(request.POST, instance=source_type) 
        else:
            source_type = forms.SaveSourceType(request.POST)    
        if source_type.is_valid():
            source_type.save()
            if post['id']:
                messages.success(request, 'Source type edited successfully')
                return redirect('source_type', 'id')
            else:
                messages.success(request, 'Source type added successfully')
        else:
            print(source_type.errors.as_text)
            for field in source_type.errors.values():
                for error in field:
                    messages.error(request, error)
    else:
        messages.error(request,'No data has been sent')
    return HttpResponseRedirect('/manage_source_type/')
    

@login_required
def delete_source_type(request, id):
    source_type = models.SourceType.objects.get(pk = id)
    source_type.delete()
    messages.success(request, 'Delete source type successfully')
    return HttpResponseRedirect('/source_type/id')

# --------LANGUAGE------------
@login_required
def language(request, order = 'id'):
    context = context_data()
    context['page_title'] = 'Languages'
    language = models.Language.objects.all().order_by(order)
    p = Paginator(language, 3)
    page = request.GET.get('page')
    language = p.get_page(page)
    context["language"] = language
    return render(request, 'ad/language.html', context)

def manage_language(request, id = None):
    context = context_data()
    context['page_title'] = 'Manage Language'
    if id:
        context['language'] = models.Language.objects.get(pk = id)
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
            language = forms.SaveLanguage(request.POST, instance=language) 
        else:
            language = forms.SaveLanguage(request.POST)
        if language.is_valid():
            language.save()
            if post['id']:
                messages.success(request, 'Language edited')
                return redirect('language', 'id')
            else:
                messages.success(request, 'New language added')
        else:
            print(language.errors.as_text)
            for field in language.errors.values():
                for error in field:
                    messages.error(request, error)
    else:
        messages.error(request, "No data has been sent")
    return HttpResponseRedirect('/manage_language/')


@login_required
def delete_language(request, id):
    language = models.Language.objects.get(pk = id)
    language.delete()
    messages.success(request,'Delete language successfully')
    return HttpResponseRedirect('/language/id')

# --------BOOK--------
@login_required
def book(request, order = 'id'):
    context = context_data()
    context['page_title'] = 'Books'
    book = models.Book.objects.all().order_by(order)
    p = Paginator(book, 3)
    page = request.GET.get('page')
    book = p.get_page(page)
    context["book"] = book
    return render(request, 'ad/book.html', context)

def manage_book(request, id = None):
    context = context_data()
    context['page_title'] = 'Manage Book'
    context['categorys'] = models.Category.objects.all()
    if id:
        context['book'] = models.Book.objects.get(pk = id)
        context['type'] = 'Save'
    else:
        context['book'] = {}
        context['type'] = 'Add'
    context['categories'] = models.Category.objects.all()
    context['source_types'] = models.SourceType.objects.all()
    context['languages'] = models.Language.objects.all()
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
            if post['id']:
                messages.success(request, 'Book edited successfully')
                return redirect('book', 'id')
            else:
                messages.success(request, 'Save book successfully')
        else:
            for field in book.errors.values():
                for error in field:
                    messages.error(request, error)
    else:
        messages.error(request, 'No data has been sent')
    return HttpResponseRedirect('/manage_book/')
    
@login_required
def delete_book(request, id):
    book = models.Book.objects.get(pk = id)
    if len(book.image) > 0:
        os.remove(book.image.path)
    book.delete()
    messages.success(request, 'Delete successfully')
    return redirect('book', 'id')

# Librarian-Librarian-Librarian-Librarian-Librarian-Librarian-Librarian-Librarian-Librarian-Librarian

# ---------LOAN Transaction-----------
@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def libhome(request):
    context = context_data()
    context["page_title"] = "Librarian Home"
    return render(request, "ad/libhome.html", context)


@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def loan(request, order = 'id'):
    context = context_data()
    context["page_title"] = "Loan Transaction"
    loans = models.LoanTransaction.objects.get_queryset().order_by(order).filter(returned = "0")
    # setup pagination
    p = Paginator(loans, 5)
    page = request.GET.get('page')
    loan_p = p.get_page(page)
    context["loan"] = loan_p
    context["readers"] = models.Profile.objects.all().filter(role = "READER")
    context["books"] = models.Book.objects.all()
    return render(request, "ad/loan.html", context)

@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def save_loan(request):
    if request.method == "POST":
        loan = forms.SaveTransaction(request.POST)
        if loan.is_valid():
            flag = loan.check_book_status()
            if not flag:
                messages.info(request, 'Book is out of quantity')
            else:
                loan.save()
                messages.success(request,'Adding New Transaction succeed')
            return redirect("loan", 'id')
        else:
            for field in loan.errors.values():
                for error in field:
                    messages.error(request, error)
                
            return redirect("loan", 'id')
    else:
        messages.error(request, 'No data has been sent')
        return redirect("loan", 'id')

@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def delete_loan(request, id):
    loan = models.LoanTransaction.objects.get(pk=id)
    loan.delete()
    book = loan.book
    book.quantity += 1
    if book.quantity == 1:
        book.status = '1'
    book.save(update_fields=['quantity', 'status'])
    messages.success(request, 'Deleting transaction succeed!')
    return redirect("loan", 'id')


@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def return_book(request, id):
    loan = models.LoanTransaction.objects.get(pk=id)
    loan.returned = '1'
    loan.save(update_fields=['returned'])
    if timezone.now() > loan.date_expired:
        loan.overdue = '1'
        messages.warning(request, 'Overdue !!!')
    else:
        loan.overdue = '0'
        messages.success(request, 'Reader returned book successfully!')
    loan.save(update_fields=['overdue'])

    book = loan.book
    book.quantity += 1
    if book.quantity == 1:
        book.status = '1'
    book.save(update_fields=['quantity', 'status'])
    return redirect("loan", 'id')

@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def renew_book(request, id):
    loan = models.LoanTransaction.objects.get(pk=id)
    loan.date_expired += timedelta(7)
    loan.save(update_fields=['date_expired'])
    messages.success(request, 'Reader renew book succeed!')
    return redirect("loan", 'id')

# -------------------ReaderInfo------------
def order_by_quantity():
    users = User.objects.all().filter(profile__identity__contains = 'RD')
    sorted(users, key=lambda x: models.LoanTransaction.objects.all().filter(user = x).count())
    return users

@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def reader_info(request, order = 'id'):
    context = context_data()
    context["page_title"] = "Reader Infomation"
    if order != 'quantity':
        users = User.objects.get_queryset().order_by(order).filter(profile__identity__contains = 'RD')
    else:
        users = order_by_quantity()
    # setup pagination
    p = Paginator(users, 5)
    page = request.GET.get('page')
    user_p = p.get_page(page)
    context["users"] = user_p
    return render(request, "ad/reader_info.html", context)

@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def request_reader(request, order = 'id'):
    context = context_data()
    context["page_title"] = "Request Reader Account"
    if request.method == "POST":
        request_reader = forms.SaveRequestReader(request.POST)
        request_reader.save()
        messages.success(request, 'Request reader account successfully!')
        return redirect('request_reader', 'id')
    else:
        requests = models.ReaderRequest.objects.all().order_by(order)
        p = Paginator(requests, 5)
        page = request.GET.get('page')
        requests = p.get_page(page)
        context["requests"] = requests
    return render(request, "ad/request_reader.html", context)

def modify_post(post):
    request = models.ReaderRequest.objects.get(pk = post['id'])
    return {
        'username' : post['username'],
        'password1' : post['password1'],
        'password2' : post['password2'],
        'first_name' : request.first_name,
        'last_name' : request.last_name,
        'email' : request.email,
        'role' : 'READER',
    }

@login_required
@allowed_users(allowed_roles=['ADMIN'])
def accept_request_reader(request):
    if request.method == "POST":
        post = modify_post(request.POST)
        user = forms.SaveUser(post)
        if user.is_valid():
            user = user.save()
            request_reader = models.ReaderRequest.objects.get(pk = request.POST['id'])
            request_reader.status = '2'
            request_reader.save(update_fields=['status'])
            messages.success(request, 'Account created successfully!')
            profile = models.Profile.objects.get(pk = user.id)
            profile = forms.SaveProfile(post, instance= profile)
            if profile.is_valid():
                profile.save()
            else:
                messages.warning(request, 'Profile fields has something wrong, must be edited later')
        else:
            for error in user.errors.values():
                messages.warning(request, error)
        return redirect("manage_reader_request", 'id')
    else:
        messages.error(request, 'No data has been sent')
        return redirect("manage_reader_request", 'id')


@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def delete_request_reader(request, id = None):
    models.ReaderRequest.objects.get(pk = id).delete()
    messages.success(request, 'Deleting reader request successfully!')
    return redirect('request_reader' , 'id')


@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def request_book(request, order = 'id'):
    context = context_data()
    context["page_title"] = "Request Book"
    requests = models.BookRequest.objects.all().order_by(order)
    categories = models.Category.objects.all()
    source_types = models.SourceType.objects.all()
    languages = models.Language.objects.all()
    p = Paginator(requests, 5)
    page = request.GET.get('page')
    requests = p.get_page(page)
    context["requests"] = requests
    context["categories"] = categories
    context["source_types"] = source_types
    context["languages"] = languages
    return render(request, "ad/request_book.html", context)

@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def save_request_book(request):
    if request.method == "POST":
        print(request.POST)
        request_book = forms.SaveRequestBook(request.POST, request.FILES)
        if request_book.is_valid():
            request_book.save()
            messages.success(request, 'Requesting book succeed!')
        else:
            for field in request_book.errors.values():
                for error in field:
                    messages.error(request, error)
        return redirect('request_book', 'id')

@login_required
@allowed_users(allowed_roles=['LIBRARIAN'])
def delete_request_book(request, id = None):
    models.BookRequest.objects.get(pk = id).delete()
    messages.success(request, 'Deleting book request successfully!')
    return redirect('request_reader' , 'id')



# ---------------------Users----------------
@login_required
@allowed_users(allowed_roles=['ADMIN'])
def user(request, order = 'id'):
    context = context_data()
    context["page_title"] = "Users"
    users = User.objects.all().order_by(order)
    p = Paginator(users, 3)
    page = request.GET.get('page')
    users = p.get_page(page)
    context["users"] = users
    return render(request, "ad/user.html", context)

@login_required
@allowed_users(allowed_roles=['ADMIN'])
def manage_user(request):
    context = context_data()
    context["page_title"] = "Manage Users"
    context["user"] = {}
    context["type"] = "Add"
    return render(request, "ad/manage_user.html", context)

@login_required
@allowed_users(allowed_roles=['ADMIN'])
def save_user(request):
    if request.method == "POST":
        user = forms.SaveUser(request.POST)
        if user.is_valid():
            user = user.save()
            messages.success(request, 'Account created successfully!')
            profile = models.Profile.objects.get(pk = user.id)
            profile = forms.SaveProfile(request.POST, instance= profile)
            if profile.is_valid():
                profile.save()
            else:
                for field in profile.errors.values():
                    for error in field:
                        messages.error(request, error)
        else:
            for error in user.errors.values():
                messages.warning(request, error)
        return redirect("user", 'id')
    else:
        messages.error(request, 'No data has been sent')
        return redirect("user", 'id')

@login_required
@allowed_users(allowed_roles=['ADMIN'])
def manage_reader_request(request, order = 'id'):
    context = context_data()
    context["page_title"] = "Manage Reader Request"
    requests = models.ReaderRequest.objects.all().order_by(order)
    p = Paginator(requests, 3)
    page = request.GET.get('page')
    requests = p.get_page(page)
    context["requests"] = requests
    return render(request, "ad/manage_reader_request.html", context)

@login_required
@allowed_users(allowed_roles=['ADMIN'])
def decline_reader_request(request, id=None):
    reader_request = models.ReaderRequest.objects.get(pk=id)
    reader_request.status = '3'
    reader_request.save(update_fields=['status'])
    messages.success(request, 'Decline successfully!')
    return redirect('manage_reader_request', 'id')

@login_required
def view_user(request, id):
    context = context_data()
    context["page_title"] = "View Categories"
    context["user"] = User.objects.get(pk=id)
    return render(request, "ad/view_user.html", context)

def homepage(request):
    context = {}
    categories = models.Category.objects.all()[0:6]
    context['categories'] = categories
    books = models.Book.objects.all()[0:12]
    context['books'] = books
    allcategory = models.Category.objects.all()
    context['allcategory'] = allcategory
    newbooks = models.Book.objects.all().order_by('-date_added')[0]
    context['newbooks'] = newbooks
    blogs = models.Post.objects.all().order_by('-created_at')[0:3]
    context['blogs'] = blogs
    blogs_footer = models.Post.objects.all().order_by('-created_at')[0:2]
    context['blogs_footer'] = blogs_footer
    context['categories_footer'] = models.Category.objects.all().order_by('-date_added')[0:4]
    return render(request,'homepage/index.html', context)

def events(request):
    context={}
    context['blogs'] = models.Post.objects.all()
    blogs_footer = models.Post.objects.all().order_by('-created_at')[0:2]
    context['blogs_footer'] = blogs_footer
    context['categories_footer'] = models.Category.objects.all().order_by('-date_added')[0:4]
    return render(request,'homepage/event.html', context)

def help(request):
    context = {}
    blogs_footer = models.Post.objects.all().order_by('-created_at')[0:2]
    context['blogs_footer'] = blogs_footer
    context['categories_footer'] = models.Category.objects.all().order_by('-date_added')[0:4]
    return render(request,'homepage/help.html', context)
    
def about(request):
    context = {}
    blogs_footer = models.Post.objects.all().order_by('-created_at')[0:2]
    context['blogs_footer'] = blogs_footer
    context['categories_footer'] = models.Category.objects.all().order_by('-date_added')[0:4]
    return render(request,'homepage/aboutus.html')

def blog(request, id = None):
    context = {}
    context['blog'] = models.Post.objects.all().get(pk = id)
    blog_recently = models.Post.objects.all().exclude(pk = id).order_by('-created_at')[0:3]
    context['blog_recently'] = blog_recently
    blogs_footer = models.Post.objects.all().order_by('-created_at')[0:2]
    context['blogs_footer'] = blogs_footer
    context['categories_footer'] = models.Category.objects.all().order_by('-date_added')[0:4]
    return render(request,'homepage/blog-single.html', context)

def profile(request, id = None):
    context = {}
    context['profile'] = models.Profile.objects.get(pk = id)
    context['booksloan'] = models.LoanTransaction.objects.all().filter(user = id).order_by('returned')
    blogs_footer = models.Post.objects.all().order_by('-created_at')[0:2]
    context['blogs_footer'] = blogs_footer
    context['categories_footer'] = models.Category.objects.all().order_by('-date_added')[0:4]
    return render(request,'homepage/profile.html',context)

def editprofile(request, id = None):
    context = {}
    context['profile'] = models.Profile.objects.get(pk = id)
    blogs_footer = models.Post.objects.all().order_by('-created_at')[0:2]
    context['blogs_footer'] = blogs_footer
    context['categories_footer'] = models.Category.objects.all().order_by('-date_added')[0:4]
    return render(request,'homepage/editprofile.html', context)

def bookdetail(request, id = None):
    context = {}
    book = models.Book.objects.all().get(pk = id)
    context['book'] = book
    context['categories']  = models.Category.objects.all()
    context['comments']  = models.Comment.objects.all().filter(book = id)
    context['bookralated'] = models.Book.objects.all().exclude(pk = id).filter(category__in = book.category.all())[0:6]
    blogs_footer = models.Post.objects.all().order_by('-created_at')[0:2]
    context['blogs_footer'] = blogs_footer
    context['categories_footer'] = models.Category.objects.all().order_by('-date_added')[0:4]
    return render(request,'homepage/book-single.html', context)

def save_comment(request, id = None):
    comment = forms.SaveComment(request.POST)
    if comment.is_valid():
        comment.save()
        messages.success(request,'Comment successfully')
    else:
        messages.error(request,'Something wrong')
    return redirect('bookdetail', id)

def filtervalue(post):
    searchs = post.split(' ')

    q_objects = [Q(category__name__contains = search) | Q(title__contains  = search)  | Q(author__contains  = search)  
                                                | Q(language__fullname__contains  = search) | Q(sourcetype__name__contains  = search)
                                                | Q(publication_year__contains  = search) for search in searchs]
    
    combined_q_objects = Q()
    for q_object in q_objects:
        combined_q_objects |= q_object

    filtered_objects = models.Book.objects.all().filter(combined_q_objects)

    return filtered_objects

def searchbook(request, cate = None):
    context = {}
    if request.method == "POST":
        books = filtervalue(request.POST['searchbox'])
    else:
        books = models.Book.objects.all()
        if cate != 0:
            books = books.filter(category = cate)
    context['books'] = books
    context['categories'] = models.Category.objects.all()
    context['languages'] = models.Language.objects.all()
    context['sourcetypes'] = models.SourceType.objects.all()
    blogs_footer = models.Post.objects.all().order_by('-created_at')[0:2]
    context['blogs_footer'] = blogs_footer
    context['categories_footer'] = models.Category.objects.all().order_by('-date_added')[0:4]
    return render(request,'homepage/book.html', context)
