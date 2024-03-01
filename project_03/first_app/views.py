from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d = {'author': 'ratul is a very polite guy', 'stripexm': '<b>I</b> <button>love</button> <span>dogs</span>', 'age': 24, 'lst': ["dhaka", "chattagram", "sylhet", "bandarban", "Rangpur"], 'heading': 'Hello &lt;i>my&lt;/i> World!', 'sentence': 'i\nhate \npretty \nu bro', 'lst2': [0, 1, 2, 3], 'birthday': datetime.datetime.now(), 'val': '','courses': [

        {
            'id': 19,
            'name': 'python',
            'fee': 20

        },
        {
            'id': 28,
            'name': 'Django',
            'fee': 50
        },
        {
            'id': 32,
            'name': 'Flask',
            'fee': 40
        },

    ]}
    return  render(request, 'home.html', context= d)