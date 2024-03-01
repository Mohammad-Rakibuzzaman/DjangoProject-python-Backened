from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Userdetails
# from .models import RegisterAccount
from .constants import GENDER_TYPE
# class AuthorForm(forms.ModelForm):
#     class Meta: 
#         model = Author
#         fields = '__all__'

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))

    

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # def save(self, commit=True):
    #     our_user = super().save(commit=False) # ami database e data save korbo na ekhn
    #     if commit == True:
    #         our_user.save() # user model e data save korlam
    #         account_type = self.cleaned_data.get('account_type')
    #         gender = self.cleaned_data.get('gender')
    #         postal_code = self.cleaned_data.get('postal_code')
    #         country = self.cleaned_data.get('country')
    #         birth_date = self.cleaned_data.get('birth_date')
    #         city = self.cleaned_data.get('city')
    #         street_address = self.cleaned_data.get('street_address')
            
    #         UserAddress.objects.create(
    #             user = our_user,
    #             postal_code = postal_code,
    #             country = country,
    #             city = city,
    #             street_address = street_address
    #         )
    #         UserBankAccount.objects.create(
    #             user = our_user,
    #             account_type  = account_type,
    #             gender = gender,
    #             birth_date =birth_date,
    #             account_no = 100000+ our_user.id
    #         )
    #     return our_user
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({
                
    #             'class' : (
    #                 'appearance-none block w-full bg-gray-200 '
    #                 'text-gray-700 border border-gray-200 rounded '
    #                 'py-3 px-4 leading-tight focus:outline-none '
    #                 'focus:bg-white focus:border-gray-500'
    #             ) 
    #         })




class ChangeUserForm(UserChangeForm):
    
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

   
class UserdetailsForm(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields = ['institution_name', 'qualifications', 'passing_year', 'gpa']