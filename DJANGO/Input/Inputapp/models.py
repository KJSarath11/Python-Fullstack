from django.db import models

# Create your models here.
class studentss(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    phno=models.PositiveIntegerField()

    def __str__(self):
        return self.name
