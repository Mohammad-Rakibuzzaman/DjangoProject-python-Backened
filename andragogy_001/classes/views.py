from django.shortcuts import render, redirect
from . import forms
# Create your views here.

def add_classes(request):
    if request.method == 'POST': 
        classes_form = forms.ClassesForm(request.POST) 
        if classes_form.is_valid():
            classes_form.save()
            return redirect('add_classes') 
    
    else: 
        classes_form = forms.ClassesForm()
    return render(request, 'add_classes.html', {'form' : classes_form})