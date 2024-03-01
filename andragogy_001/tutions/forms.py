from django import forms
from .models import Tution, Comment, Applicant

class TutionForm(forms.ModelForm):
    class Meta: 
        model = Tution
        # fields = '__all__'
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name','body']

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = [] 

