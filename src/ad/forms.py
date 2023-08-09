from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from django.db.models import Q
from datetime import datetime
from django.utils import timezone

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class SaveUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self,data = None, *args, **kwargs):
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
        email = self.cleaned_data['email']
        try:
            models.Profile.objects.get(email = email)
            self.add_error('email', forms.ValidationError('Email is already taken!'))
        except:
            return email

class EditProfile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('first_name','last_name','email','phone','date_of_birth','sex','bio')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            models.Profile.objects.exclude(id = self.instance.id).get(email = email)
            self.add_error('email', forms.ValidationError('Email is already taken!'))
        except:
            return email

class EditAvatar(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ('profile_img',)

class SaveCategory(forms.ModelForm):
    name = forms.CharField(max_length=250)
    description = forms.Textarea()
    image = forms.ImageField()
    class Meta:
        model = models.Category
        fields = ('name', 'description', 'image')

    def clean(self):
        id = self.data['id'] if (self.data['id']).isnumeric() else 0
        name = self.data.get('name')
        cleaned_data = self.cleaned_data
        try:
            if int(id) > 0:
                models.Category.objects.exclude(id=id).get(name=name)
            else:
                models.Category.objects.get(name=name)
            self.add_error('name',forms.ValidationError('This category name already exists.'))
        except:
            return cleaned_data
    
class SaveSourceType(forms.ModelForm):
    code = forms.CharField(max_length=50)
    name = forms.CharField(max_length=250)
    description = forms.Textarea()

    class Meta:
        model = models.SourceType
        fields = ('code', 'name', 'description', )

    def clean(self):
        id = self.data['id'] if (self.data['id']).isnumeric() else 0
        code = self.data.get('code')
        cleaned_data = self.cleaned_data
        try:
            if int(id) > 0:
                models.SourceType.objects.exclude(id=id).get(code=code)
            else:
                models.SourceType.objects.get(code=code)
            self.add_error('code',forms.ValidationError('This source type code already exists.'))
        except:
            return cleaned_data

class SaveLanguage(forms.ModelForm):
    code = forms.CharField(max_length=50)
    fullname = forms.CharField(max_length=250)

    class Meta:
        model = models.Language
        fields = ('code', 'fullname', )

    def clean(self):
        id = self.data['id'] if (self.data['id']).isnumeric() else 0
        code = self.data.get('code')
        cleaned_data = self.cleaned_data
        try:
            if int(id) > 0:
                models.Language.objects.exclude(id=id).get(code=code)
            else:
                models.Language.objects.get(code=code)
            self.add_error('code',forms.ValidationError('This language code already exists.'))
        except:
            return cleaned_data

class SaveBook(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = ('title', 'publication_year', 'author', 'category', 'description', 'sourcetype', 'language', 'image', 'quantity',)

    def cleanTitle(self, title):
        id = self.data['id'] if (self.data['id']).isnumeric() else 0
        title = self.data.get('title')
        if int(id) > 0 and title in models.Book.objects.exclude(id=id).values_list('title', flat=True):
            self.add_error('title',forms.ValidationError('This book title already exists.'))
            return False
        elif int(id)==0 and title in models.Book.objects.values_list('title', flat=True):
            self.add_error('title',forms.ValidationError('This book title already exists.'))
            return False
        else:
            return True

    def cleanYear(self, year):
        if int(year) > timezone.now().year:
            self.add_error('publication_year',forms.ValidationError('Publication year exceeds current year.'))
            return False
        else:
            return True

    def cleanQuantity(self, quantity):
        if int(quantity) < 0:
            self.add_error('quantity',forms.ValidationError('The book quantity is smaller than 0.'))
            return False
        else:
            return True

    def clean(self):
        cleaned_data = self.cleaned_data

        # print(self.data)
        # print(cleaned_data)
        
        title = self.data.get('title')
        self.cleanTitle(title)
        
        publication_year = self.data.get('publication_year')
        self.cleanYear(publication_year)

        quantity = self.data.get('quantity')
        self.cleanQuantity(quantity)


class SaveRequestBook(forms.ModelForm):
    class Meta:
        model = models.BookRequest
        fields  = ('title', 'publication_year', 'author', 'category', 'description', 'sourcetype', 'language', 'image')
        

class SaveTransaction(forms.ModelForm):
    # user = forms.ModelChoiceField(queryset=User.objects.all())
    # book = forms.ModelChoiceField(queryset=models.Book.objects.all())
    class Meta:
        model = models.LoanTransaction
        fields = ('user','book')

    def __init__(self,data = None, *args, **kwargs):
        try:
            profile = models.Profile.objects.get(identity = data['identity'])
            user = User.objects.get(pk = profile.id)
        except:
            user = None
        try:
            book = models.Book.objects.get(title = data['book'])
        except:
            book = None
        new_data = {'user': user, 'book': book}
        super().__init__(new_data, *args, **kwargs)
        
    def clean(self):
        user = self.data.get('user')
        book = self.data.get('book')

        if user not in User.objects.all():
            self.add_error('user', forms.ValidationError('The user is not existed'))
            self.errors['user'].pop(0)
        else:
            if 'RD' not in user.profile.identity:
                self.add_error('user', forms.ValidationError('The user is not available'))

        if book not in models.Book.objects.all():
            self.add_error('book', forms.ValidationError('The book is not existed'))
            self.errors['book'].pop(0)

        try:
            loan = models.LoanTransaction.objects.get(user= user, book = book)
            if loan.date_loan <= timezone.now():
                if loan.returned == '0':
                    self.add_error('book', forms.ValidationError('Reader has not returned this book yet!'))
                    print(1)
        except:
            return {'user': user, 'book' : book}

    def check_book_status(self):
        book = self.data['book']
        if book.status == '1':
            book.quantity -= 1
            if book.quantity == 0:
                book.status = '2'
                book.save(update_fields = ['status'])
            book.save(update_fields = ['quantity'])
            return 1
        else:
            return 0

class SaveComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('user','book','content')

