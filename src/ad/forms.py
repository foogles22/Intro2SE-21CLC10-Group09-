from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
from . import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.MyUser
        fields = ('username','password1','password2')
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = models.MyUser
        fields = ('username','email','role','phone','sex','date_of_birth')

class SaveCategory(forms.ModelForm):
    # name = forms.CharField(max_length=250)
    # description = forms.Textarea()
    # status = forms.CharField(max_length=2)

    class Meta:
        model = models.Category
        fields = ('name', 'description', 'status', )

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

