from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


# -User-User--User--User--User--User--User--User--User--User--User--User--User--User--User--User--User--User-

class MyUser(AbstractUser):
    date_of_birth = models.DateField(default=timezone.now)
    sex = models.CharField(max_length=2, choices=(("1", "Male"),("2", "Female")))
    phone = models.CharField(max_length=15, blank= True, null=True)
    
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        LIBRARIAN = "LIBRARIAN", 'Librarian'
        READER = "READER", 'Reader'

    base_role = Role.READER

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *arg, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*arg,**kwargs)

class LibrarianManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs):
        results = super().ger_queryset(*args,**kwargs)
        return results.filter(role=MyUser.Role.LIBRARIAN)

class Librarian(MyUser):
    base_role = MyUser.Role.LIBRARIAN
    object = LibrarianManager()
    class Meta:
        proxy = True

class AdminManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs):
        results = super().ger_queryset(*args,**kwargs)
        return results.filter(role=MyUser.Role.ADMIN)
    
class Admin(MyUser):
    base_role = MyUser.Role.ADMIN

    class Meta:
        proxy = True
# -ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN-ADMIN
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=2, choices=(("1", "Active"), ("2", "Inactive")), default=1
    )
    delete_flag = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(f"{self.name}")


class SourceType(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    delete_flag = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(f"{self.name}")


class Language(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    fullname = models.CharField(max_length=250)
    delete_flag = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(f"{self.fullname}")


class Book(models.Model):
    title = models.CharField(primary_key=True, max_length=250)
    publication_year = models.DateField()
    author = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    sourcetype = models.ForeignKey(SourceType, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    image = models.ImageField()
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=2, choices=(("1", "Active"), ("2", "Inactive")), default=1
    )
    delete_flag = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(f"{self.title}")
