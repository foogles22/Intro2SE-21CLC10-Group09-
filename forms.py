from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.db.models import Q
from datetime import date
from django.utils import timezone


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class SaveUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, data = None, *args, **kwargs):
        new_data = {'username': data['username'], 'password1': data['password1'], 'password2': data['password2']}
        super().__init__(new_data, *args, **kwargs)

class SaveProfile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('first_name','last_name','email','first_time','role','identity')

    def init_identity(self, role):
        if role == "ADMIN":
            name = 'AD'
        if role == "LIBRARIAN":
            name = 'LB'
        if role == "READER":
            name = 'RD'
        return name + str(models.Profile.objects.filter(role=role).count())
    
    def __init__(self,data = None, *args, **kwargs):
        new_data = {
            'first_name': data['first_name'],
            'last_name': data['last_name'],
            'email' : data['email'],
            'first_time' : False,
            'role' : data['role'],
            'identity' : self.init_identity(data['role'])
            }
        super().__init__(new_data, *args, **kwargs)
    
    def clean_email(self):
        email = self.clean_data['email']
        try:
            models.Profile.objects.get(email = email)
            self.add_error(forms.ValidationError('email', 'Email is already taken!'))
        except:
            return email

class SaveRequestReader(forms.ModelForm):
    class Meta:
        model = models.ReaderRequest
        fields = ('first_name','last_name','email')

class EditProfile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('first_name','last_name','email','phone','date_of_birth','sex','profile_img')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            models.Profile.objects.get(email = email)
            self.add_error(forms.ValidationError('email', 'Email is already taken!'))
        except:
            return email
