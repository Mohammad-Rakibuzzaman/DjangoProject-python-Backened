from django.db import models
# from django.contrib.auth.models import User, AbstractUser
# from .constants import GENDER_TYPE
from django.contrib.auth.models import User


# class RegisterAccount(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)

#     birth_date = models.DateField(null=True, blank=True)
#     gender = models.ChoiceField(max_length=10, choices=GENDER_TYPE)
#     street_address = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=15)

#     def __str__(self):
#         return str(self.first_name)

class Userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    institution_name = models.CharField(max_length=100)
    qualifications = models.CharField(max_length=100)
    passing_year = models.CharField(max_length=15)
    gpa = models.CharField(max_length=15)
    

    def __str__(self):
        return f"{self.institution_name}"