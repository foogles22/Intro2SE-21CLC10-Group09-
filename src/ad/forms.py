from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class SaveCategory(forms.ModelForm):
    # name = forms.CharField(max_length=250)
    # description = forms.Textarea()
    # status = forms.CharField(max_length=2)

    class Meta:
        model = models.Category
        fields = ('name', 'description', 'status', )

class UserFormRegister(UserCreationForm):
    class meta:
        model = User
        fields = ('username', 'password1', 'password2')

        # widgets = {
        #     'username' : forms.CharField(attrs={'class' : 'form-control', 'id':'username'}), 
        #     'password1' : forms.CharField(attrs={'class' : 'form-control', 'id':'password1'}), 
        #     'password2' : forms.CharField(attrs={'class' : 'form-control', 'id':'password2'}), 
        # }

class SaveSourceType(forms.ModelForm):
    class Meta:
        model = models.SourceType
        fields = ('code', 'name', 'description',)


class SaveLanguage(forms.ModelForm):
    class Meta:
        model = models.Language
        fields = ('code','fullname',)
        
class SaveBook(forms.ModelForm):
    class Meta:
        model = models.Book
        fields  = ('title', 'publication_year', 'author', 'category', 'description', 'sourcetype', 'language', 'image', 'quantity', 'status')

