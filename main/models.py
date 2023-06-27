from django.db import models

class Person(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField('Описание')
    age = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='person')

    def __str__(self):
        return self.name

