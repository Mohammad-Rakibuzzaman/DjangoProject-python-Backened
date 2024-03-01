from django import forms
from first_app.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'

        fields = ['roll', 'name', 'address', 'big_integer_field', 'date_field']

        labels = {
            'name' : 'Student Name',
            'roll' : "Student Roll",
            'big_integer_field' : "Nid Number",
            'date_field' : "Joining date",
        }
        widgets  = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : "Write your full name"
        }
        
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }
