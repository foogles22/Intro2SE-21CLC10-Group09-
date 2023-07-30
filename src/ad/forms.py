from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class EditProfile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('first_name','last_name','email','phone','date_of_birth','sex','profile_img')

class SaveCategory(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ('name', 'description')

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

class SaveTransaction(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    book = forms.ModelChoiceField(queryset=models.Book.objects.all())
    class Meta:
        model = models.LoanTransaction
        fields = ('user','book')

    def __init__(self,data = None, *args, **kwargs):
        try:
            profile = models.Profile.objects.get(identity = data['identity'])
            user = User.objects.get(pk = profile.id)
        except:
            user = None
        new_data = {'user': user, 'book': data['book']}
        super().__init__(new_data, *args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('user')
        book = cleaned_data.get('book')
        if not user:
            self.add_error('user', forms.ValidationError('The user is not existed'))
            self.errors['user'].pop(0)

        if not book:
            self.add_error('book', forms.ValidationError('The book is not existed'))
            self.errors['book'].pop(0)  

    def check_book_status(self):
        book = self.cleaned_data['book']
        if book.status == '1':
            book.quantity -= 1
            if book.quantity == 0:
                book.status = '2'
                book.save(update_fields = ['status'])
            book.save(update_fields = ['quantity'])
            return 1
        else:
            return 0

