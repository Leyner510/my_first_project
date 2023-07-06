from django.db import models

class Person(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField('Описание')
    def __str__(self):
        return self.name



