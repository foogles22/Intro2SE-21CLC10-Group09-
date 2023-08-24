from . import models
from . import forms
from .decorators import user_is_authenticated, allowed_users
import csv
from datetime import timedelta
from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.http import JsonResponse
from django.utils import timezone
from pathlib import Path
import os
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

@login_required
def edit_profile(request, id):
    context = context_data()
    context["page_title"] = "Edit Profile"
    if request.method == "POST":
        profile = models.Profile.objects.get(pk = id)
        profile.first_time = False
        profile.save()
        profile = forms.EditProfile(request.POST, request.FILES , instance = profile)
        if profile.is_valid():
            profile.save()
            messages.success(request, 'Edited profile successfully')
        else:
            for field in profile.errors.values():
                for error in field:
                    messages.error(request, error)
    context["profile"] = models.Profile.objects.get(pk = id)
    return render(request, 'ad/edit_profile.html', context)


@login_required
@allowed_users(allowed_roles=['ADMIN'])
def delete_user(request, id):
    user = User.objects.get(pk = id)
    messages.success(request, 'Deleting acount succeed')
    user.delete()
    return redirect("user")
