from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(SourceType)
admin.site.register(Language)
admin.site.register(Book)
