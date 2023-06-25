from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.SourceType)
admin.site.register(models.Language)
admin.site.register(models.Book)
