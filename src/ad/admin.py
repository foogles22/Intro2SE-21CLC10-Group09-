from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(SourceType)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(LoanTransaction)
admin.site.register(Comment)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)