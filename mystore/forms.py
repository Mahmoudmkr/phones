from django import forms
from . import models

attrs= {'class':'form-control'}
class PhonesCreateForm(forms.ModelForm):
    class Meta:
        model=models.Phones
        fields=['category','title','description']
        widgets={
            'category':forms.Select(attrs=attrs),
            'title':forms.TextInput(attrs=attrs),
            'description':forms.Textarea(attrs=attrs)
        }

class PhonesUpdateForm(forms.ModelForm):
    class Meta:
        model=models.Phones
        fields=['category','title','status']
        widgets={
            'category':forms.Select(attrs=attrs),
            'title':forms.TextInput(attrs=attrs),
            'status':forms.Select(attrs=attrs)
        }