from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null= True)
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str(f'{self.name}')

class SourceType(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null= True)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)

    
    def __str__(self):
        return str(f'{self.name}')
    
class Language(models.Model):
    code = models.CharField(primary_key=True, max_length=50)
    fullname = models.CharField(max_length=250)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)

    
    def __str__(self):
        return str(f'{self.fullname}')
    
class Book(models.Model):
    title = models.CharField(primary_key=True, max_length=250)
    publication_year = models.DateField()
    author = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null= True)
    sourcetype = models.ForeignKey(SourceType, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    image = models.ImageField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str(f'{self.title}')