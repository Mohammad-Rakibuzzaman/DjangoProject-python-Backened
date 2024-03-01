from django.db import models

# Create your models here.

class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length= 20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    date_field = models.DateField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    # file_path_field = models.FilePathField(path='/path/to/files/')
    generic_ip_address_field = models.GenericIPAddressField()
    json_field = models.JSONField()
    slug_field = models.SlugField()
    uuid_field = models.UUIDField()


    def __str__(self):
        return f"Name: {self.name}"