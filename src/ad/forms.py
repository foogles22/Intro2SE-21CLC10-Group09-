from django import forms
from . import models

class SaveCategory(forms.ModelForm):
    name = forms.CharField(max_length=250)
    description = forms.Textarea()
    class Meta:
        model = models.Category
        fields = ('name', 'description', )

    def clean(self):
        name = self.data.get('name')
        description = self.data.get('description')
        try:
            models.Category.objects.get(pk=name)
            self.add_error('name',forms.ValidationError('This category name already exists.'))
            self.errors['name'].pop(0)
        except:
            return {'name':name, 'description':description}

class EditCategory(forms.ModelForm):
    name = forms.CharField(max_length=250)
    description = forms.Textarea()
    class Meta:
        model = models.Category
        fields = ('name', 'description', )
    
class SaveSourceType(forms.ModelForm):
    code = forms.CharField(max_length=50)
    name = forms.CharField(max_length=250)
    description = forms.Textarea()

    class Meta:
        model = models.SourceType
        fields = ('code', 'name', 'description', )

    def clean(self):
        code = self.data.get('code')
        name = self.data.get('name')
        description = self.data.get('description')
        try:
            models.SourceType.objects.get(code=code)
            self.add_error('code',forms.ValidationError('This source type code already exists.'))
            self.errors['code'].pop(0)
        except:
            return {'code': code, 'name':name, 'description':description}


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
        code = self.data.get('code')
        fullname = self.data.get('fullname')
        try:
            models.Language.objects.get(code=code)
            self.add_error('code',forms.ValidationError('This language code already exists.'))
            self.errors['code'].pop(0)
        except:
            return {'code': code, 'fullname':fullname}


class EditLanguage(forms.ModelForm):
    code = forms.CharField(max_length=50)
    fullname = forms.CharField(max_length=250)

    class Meta:
        model = models.Language
        fields = ('code', 'fullname', )


class SaveBook(forms.ModelForm):
    title = forms.CharField(max_length=250)
    publication_year = forms.DateField()
    author = forms.CharField(max_length=250)
    category = forms.ModelMultipleChoiceField(queryset=models.Category.objects.all())
    description = forms.Textarea()
    sourcetype = forms.ModelChoiceField(queryset=models.SourceType.objects.all(), to_field_name=models.SourceType.code)
    language = forms.ModelChoiceField(queryset=models.Language.objects.all(), to_field_name=models.Language.code)
    image = forms.ImageField()
    quantity = forms.IntegerField()

    class Meta:
        model = models.Book
        fields = ('title', 'publication_year', 'author', 'category', 'description', 'sourcetype', 'language', 'image', 'quantity',)