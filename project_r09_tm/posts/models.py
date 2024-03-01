from django.db import models
from categories.models import TaskCategory
# Create your models here.

class TaskModel(models.Model):
    # title, description, is_completed by def false, date
    title =  models.CharField(max_length=50)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    date = models.DateField()
    category = models.ManyToManyField(TaskCategory)

    def __str__(self):
        return self.title
