from django import forms
from django.core import validators

#widgets == field to html input
#we can also use charfield if we dont remember functions
class contactForm(forms.Form):
    #  disbled= True , initial = "Rahim"
    name = forms.CharField(label="Full Name: ", help_text="Enter full name within 70 characters",
                    required= False, widget= forms.Textarea(attrs = {"id": "text_area", "class": "class1 class2", "placeholder":"Enter your name"}))
    # file = forms.FileField()
    email = forms.EmailField(label="User Mail")
    age = forms.IntegerField(widget=forms.NumberInput)
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget= forms.DateInput(attrs= {"type": "date"} ))
    appointment = forms.DateTimeField(widget= forms.DateInput(attrs= {"type": "datetime-local"} ))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget= forms.RadioSelect)
    MEAL = [('P', 'Pepper'), ('M', 'Mashroom'), ('B', 'Baskroom')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget= forms.CheckboxSelectMultiple)
    
# class StudentData(forms.Form):
#     name = forms.CharField(widget= forms.TextInput)
#     email = forms.CharField(widget= forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name with at least 10 characters")
#     #     return valname
    
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("You must provide an email address with .com in your email")
#     #     return valemail

#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']

#         valname = self.cleaned_data['name']
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name with at least 10 characters")
     

#         valemail = self.cleaned_data['email']
#         if '.com' not in valemail:
#             raise forms.ValidationError("You must provide an email address with .com in your email")

def len_check(value):
    if len(value) < 10:
        raise forms.ValidationError("Please provide at least 10 chars")


class StudentData(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10, message= "pls enter value max 10 characters")])
    
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])

    email = forms.CharField(widget= forms.EmailInput, validators=[validators.EmailValidator(message= "pls enter valid email")])       
    age = forms.IntegerField(validators= [validators.MaxValueValidator(34, message="age must be below to 34!"), validators.MinValueValidator(24, message="age should above 24!")])       
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg'], message= "file must contain .pdf extension")])

class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget= forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    #for practice
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)


    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data["password"]
        val_conpass = self.cleaned_data["confirm_password"] 
        val_name = self.cleaned_data['name']
        
        
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match!")
        
        if len(val_name) < 15:
            raise forms.ValidationError("Name must be at least 15 characters")