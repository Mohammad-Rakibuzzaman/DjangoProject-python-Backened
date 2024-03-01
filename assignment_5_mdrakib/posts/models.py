from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    image = models.ImageField(upload_to = 'posts/media/uploads/', blank = True, null = True)
    borrowing_price = models.DecimalField(default=None, max_digits=10, decimal_places = 2)
    user_reviews = models.TextField(null= True, blank = True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) #jokhon obj create hobe time janay dibe

    def __str__(self):
        return f"Commented by {self.name}"