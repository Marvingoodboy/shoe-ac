from django.conf import settings
from django.db import models
from datetime import datetime


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Shoe(models.Model):
    MALE = [
        ('Man', 'Man'),
        ('Woman', 'Woman'),
        ('Child', 'Child')
    ]
    SEASON = [
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall or Autumn', 'Fall or Autumn'),
        ('Winter', 'Winter'),
    ]

    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    size = models.PositiveSmallIntegerField()
    quantity = models.PositiveSmallIntegerField()
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    season = models.CharField(max_length=50, choices=SEASON, default=1)
    model = models.CharField(max_length=50)
    male = models.CharField(max_length=50, choices=MALE, default=1)
    image = models.ImageField(upload_to='media', default=None)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    dateAndTime = models.DateTimeField(default=datetime.now())
