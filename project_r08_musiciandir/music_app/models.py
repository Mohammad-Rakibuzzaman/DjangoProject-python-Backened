from django.db import models

# Create your models here.

class Musician(models.Model):
    # id = models.IntegerField(primary_key=True)
    # id = models.IntegerField(primary_key= True)
    name = models.CharField(max_length= 60)
    lastname = models.CharField(max_length= 50)
    email_field = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.name} - {self.lastname}"

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(choices = [(i, i) for i in range(1, 6)])
    album = models.ForeignKey(Musician, on_delete = models.CASCADE, default=None)

    def __str__(self):
        return f"{self.album_name}"
