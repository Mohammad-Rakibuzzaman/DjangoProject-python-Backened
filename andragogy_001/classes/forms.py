from django import forms
from .models import Classes

class ClassesForm(forms.ModelForm):
    class Meta: 
        model = Classes
        fields = '__all__'