from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length= 20)
    roll = models.IntegerField(primary_key = True)
    address = models.TextField()
    
    big_integer_field = models.BigIntegerField(null=True)
    binary_field = models.BinaryField(null=True)
    boolean_field = models.BooleanField(null=True)    
    date_field = models.DateField(null=True)
    date_time_field = models.DateTimeField(null=True)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    duration_field = models.DurationField(null=True)
    email_field = models.EmailField(null=True)
    # file_field = models.FileField(upload_to='files/')
    float_field = models.FloatField(null=True)


    def __str__(self):
        return f"Roll : {self.roll} - {self.name}"





#username = rtza pass = 1234
    
