from django import forms
from . import models
from django.utils import timezone

class SaveCategory(forms.ModelForm):
    name = forms.CharField(max_length=250)
    description = forms.Textarea()
    image = forms.ImageField()
    class Meta:
        model = models.Category
        fields = ('name', 'description', 'image')

    def clean(self):
        cleaned_data = self.cleaned_data
        name = cleaned_data['name']
        try:
            models.Category.objects.get(pk=name)
            self.add_error('name',forms.ValidationError('This category name already exists.'))
            self.errors['name'].pop(0)
        except:
            return cleaned_data

class EditCategory(forms.ModelForm):
    name = forms.CharField(max_length=250)
    description = forms.Textarea()
    class Meta:
        model = models.Category
        fields = ('name', 'description', 'image')
    
class SaveSourceType(forms.ModelForm):
    code = forms.CharField(max_length=50)
    name = forms.CharField(max_length=250)
    description = forms.Textarea()

    class Meta:
        model = models.SourceType
        fields = ('code', 'name', 'description', )

    def clean(self):
        cleaned_data = self.cleaned_data
        code = self.data.get('code')
        try:
            models.SourceType.objects.get(code=code)
            self.add_error('code',forms.ValidationError('This source type code already exists.'))
            self.errors['code'].pop(0)
        except:
            return cleaned_data

class EditSourceType(forms.ModelForm):
    code = forms.CharField(max_length=50)
    name = forms.CharField(max_length=250)
    description = forms.Textarea()

    class Meta:
        model = models.SourceType
        fields = ('code', 'name', 'description', )

class SaveLanguage(forms.ModelForm):
    code = forms.CharField(max_length=50)
    fullname = forms.CharField(max_length=250)

    class Meta:
        model = models.Language
        fields = ('code', 'fullname', )

    def clean(self):
        cleaned_data = self.cleaned_data
        code = self.data.get('code')
        try:
            models.Language.objects.get(code=code)
            self.add_error('code',forms.ValidationError('This language code already exists.'))
            self.errors['code'].pop(0)
        except:
            return cleaned_data

class EditLanguage(forms.ModelForm):
    code = forms.CharField(max_length=50)
    fullname = forms.CharField(max_length=250)

    class Meta:
        model = models.Language
        fields = ('code', 'fullname', )

class SaveBook(forms.ModelForm):
    title = forms.CharField(max_length=250)
    publication_year = forms.IntegerField(max_value=timezone.now().year)
    author = forms.CharField(max_length=250)
    category = forms.ModelMultipleChoiceField(queryset=models.Category.objects.all())
    description = forms.Textarea()
    sourcetype = forms.ModelChoiceField(queryset=models.SourceType.objects.all())
    language = forms.ModelChoiceField(queryset=models.Language.objects.all())
    image = forms.ImageField()
    quantity = forms.IntegerField(min_value = 0)

    class Meta:
        model = models.Book
        fields = ('title', 'publication_year', 'author', 'category', 'description', 'sourcetype', 'language', 'image', 'quantity',)

    def cleanYear(self, year):
        if int(year) > timezone.now().year:
            self.add_error('publication_year',forms.ValidationError('Publication year exceeds current year.'))
            self.errors['publication_year'].pop(0)
            return False
        else:
            return True

    def cleanTitle(self, title):
        if title in models.Book.objects.values_list('title', flat=True):
            self.add_error('title',forms.ValidationError('This book title already exists.'))
            self.errors['title'].pop(0)
            return False
        else:
            return True
    
    def cleanQuantity(self, quantity):
        if int(quantity) < 0:
            self.add_error('quantity',forms.ValidationError('The book quantity is smaller than 0.'))
            self.errors['quantity'].pop(0)
            return False
        else:
            return True
    
    def clean(self):
        cleaned_data = self.cleaned_data

        title = self.data.get('title')
        self.cleanTitle(title)
        
        publication_year = self.data.get('publication_year')
        self.cleanYear(publication_year)
        
        quantity = self.data.get('quantity')
        self.cleanQuantity(quantity)
        
        return cleaned_data

class EditBook(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ('title', 'publication_year', 'author', 'category', 'description', 'sourcetype', 'language', 'image', 'quantity',)
    
    def cleanYear(self, year):
        if int(year) > timezone.now().year:
            self.add_error('publication_year',forms.ValidationError('Publication year exceeds current year.'))
            self.errors['publication_year'].pop(0)
            return False
        else:
            return True
        
    def cleanTitle(self, title):
        try:
            models.Book.objects.exclude(title=self.instance).get(title=title)
            self.add_error('title',forms.ValidationError('This book title already exists.'))
            self.errors['title'].pop(0)
            return False
        except:
            return True
    
    def cleanQuantity(self, quantity):
        if int(quantity) < 0:
            self.add_error('quantity',forms.ValidationError('The book quantity is smaller than 0.'))
            self.errors['quantity'].pop(0)
            return False
        else:
            return True
    def clean(self):
        cleaned_data = self.cleaned_data
        
        title = self.data.get('title')
        self.cleanTitle(title)
        
        publication_year = self.data.get('publication_year')
        self.cleanYear(publication_year)
        
        quantity = self.data.get('quantity')
        self.cleanQuantity(quantity)
        
        return cleaned_data