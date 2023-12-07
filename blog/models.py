from django.db import models
import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date = models.DateTimeField(default=datetime.date.today)

    def __str__(self) -> str:
        return self.title
    