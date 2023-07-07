from django import forms
from . import models

class SaveCategory(forms.ModelForm):
    name = forms.CharField(max_length=250)
    description = forms.Textarea()
    status = forms.CharField(max_length=2)

    class Meta:
        model = models.Category
        fields = ('name', 'description', 'status', )

    # def clean_name(self):
    #     id = self.data['id'] if (self.data['id']).isnumeric() else 0
    #     name = self.cleaned_data['name']
    #     try:
    #         if id > 0:
    #             category = models.Category.objects.exclude(id = id).get(name = name, delete_flag = 0)
    #         else:
    #             category = models.Category.objects.get(name = name, delete_flag = 0)
    #     except:
    #         return name
    #     raise forms.ValidationError("Category Name already exists.")


class SaveSourceType(forms.ModelForm):
    name = forms.CharField(max_length=250)
    description = forms.Textarea()
    st_code = forms.CharField(max_length=5)

    class Meta:
        model = models.SourceType
        fields = ('name', 'description', 'st_code', )