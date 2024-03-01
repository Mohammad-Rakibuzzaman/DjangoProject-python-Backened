from django.shortcuts import render
from tutions.models import Tution
from classes.models import Classes

from tutions.models import Comment

def home(request, classes_slug = None):
    data = Tution.objects.all()
    
    if classes_slug is not None:
        classes = Classes.objects.get(slug = classes_slug)
        data = Tution.objects.filter(classes  = classes)
    classes = Classes.objects.all()

    comment = Comment.objects.all()

    return render(request, 'home.html', {'data' : data, 'classes' : classes, 'Comment' : comment})