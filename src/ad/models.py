from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(blank=False, null=False, max_length=250)
    description = models.TextField(blank=True, null=True, max_length=250)
    date_added = models.DateTimeField(null=False, default=timezone.now)
    image = models.ImageField(null=False, blank=False, upload_to="images/")
    def __str__(self):
        return str(f"{self.name}")


class SourceType(models.Model):
    code = models.CharField(blank=False, null=False, max_length=50)
    name = models.CharField(null= False, blank=False, max_length=250)
    description = models.TextField(blank=True, null=True, max_length=250)
    date_added = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return str(f"{self.name}")


class Language(models.Model):
    code = models.CharField(max_length=50)
    fullname = models.CharField(null= False, blank=False, max_length=250)
    date_added = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        return str(f"{self.fullname}")


class Book(models.Model):
    title = models.CharField(blank=False, null=False, max_length=250)
    publication_year = models.IntegerField(null= False, blank=False, validators=[MaxValueValidator(timezone.now().year)])
    author = models.CharField(null= False, blank=False, max_length=250)
    category = models.ManyToManyField(Category)
    description = models.TextField(blank=True, null=True)
    sourcetype = models.ForeignKey(SourceType, on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=False, blank=False, upload_to="images/")
    quantity = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0)])
    status = models.CharField(
        max_length=2, choices=(("1", "Active"), ("2", "Inactive")), default=1
    )
    date_added = models.DateTimeField(null=False, default=timezone.now)

    def __str__(self):
        words = self.title.split()
        abbreviations = [word[0].upper() for word in words if word]
        return ''.join(abbreviations)