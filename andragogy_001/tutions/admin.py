from django.contrib import admin
from . import models
from .models import Applicant
# Register your models here.
admin.site.register(models.Tution)
admin.site.register(models.Comment)
admin.site.register(Applicant)