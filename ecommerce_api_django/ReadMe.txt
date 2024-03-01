python -m venv .venv
from fast to last all code ---

 django-admin startproject EcomApi

cd EcomApi


python manage.py startapp EcomApp


installed packages for this : 
pip install django
pip install djangorestframework
python -m pip install django-cors-headers
pip install --upgrade djangorestframework-simplejwt

1) model declare
2) register on admin.py
3) python manage.py makemigrations / migrate
4) make a serializers to convert json
5)then i have created views.py 2- list detail
6) after creating all the views.py file now its time to import
   all the views.py functions to app/ urls.py file
7) If error - just python manage.py makemigrations / migrate
8) then  - createsuperuser python manage.py createsuperuser

9)  Then I am going to install the corsheaders package : 
10) then setup corsheaders config in settings.py

+ create a cart model
+ create a cartserializer
+ create cart list and detail view
+ our api has authentication and setup up no so he is careful
  when we make request

