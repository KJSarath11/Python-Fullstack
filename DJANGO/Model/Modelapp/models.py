from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=1000)
    age=models.PositiveIntegerField()
    phno=models.PositiveIntegerField()

    def __str__(self):
        return self.name #this displays in the order of name rather than object
    
class bike(models.Model):
    name=models.CharField(max_length=1000)
    company=models.CharField(max_length=1000)
    model=models.CharField(max_length=1000)
    colour=models.CharField(max_length=1000)
    cc=models.PositiveIntegerField()
    bhp=models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class anime(models.Model):
    name=models.CharField(max_length=100)
    mc=models.CharField(max_length=100)
    episodes=models.IntegerField()

    def __str__(self):
        return self.mc

class myself(models.Model):
    name=models.CharField(max_length=100)
    hobby=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)

    def __str__(self):
        return self.hobby
