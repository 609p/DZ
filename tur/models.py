from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.CharField(max_length=100, default='') 
    content = models.TextField(default='')

    def __str__(self):
        return self.title