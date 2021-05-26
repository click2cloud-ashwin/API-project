from django.db import models


# Create your models here.

class ApiModel(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.CharField(default='average', max_length=50)

    def __str__(self):
        return self.name
