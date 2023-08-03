from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=250)
    description = models.TextField(blank=True, null=True, max_length=250)
    date_added = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return str(f"{self.name}")


class SourceType(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(null= False, blank=False, max_length=250)
    description = models.TextField(blank=True, null=True, max_length=250)
    date_added = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return str(f"{self.name}")


class Language(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    fullname = models.CharField(null= False, blank=False, max_length=250)
    date_added = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return str(f"{self.fullname}")


class Book(models.Model):
    title = models.CharField(primary_key=True, max_length=250)
    publication_year = models.DateField(null= False, blank=False)
    author = models.CharField(null= False, blank=False, max_length=250)
    category = models.ManyToManyField(Category)
    description = models.TextField(blank=True, null=True)
    sourcetype = models.ForeignKey(SourceType, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=False, upload_to="images/")
    quantity = models.IntegerField(null=False, blank=False)
    status = models.CharField(
        max_length=2, choices=(("1", "Active"), ("2", "Inactive")), default=1
    )
    date_added = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        words = self.title.split()
        abbreviations = [word[0].upper() for word in words if word]
        return ''.join(abbreviations)