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
