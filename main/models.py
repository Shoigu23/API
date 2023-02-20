from django.db import models

# Create your models here.

class Students(models.Model):
    DIRECTIONS = (
        ('Backend', 'Back-End'),
        ('FrontEnd', 'Front-End'),
        ('Fullstack', 'Fullstack'),
        ('UX/UI', 'UX/UI'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Famale', 'Famale')
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    directions = models.CharField(max_length=1500, choices=DIRECTIONS)
    gender = models.CharField(max_length=10,choices=GENDER)
