from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)

    def __str__(self):
        return self.name