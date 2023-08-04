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

        return cleaned_data