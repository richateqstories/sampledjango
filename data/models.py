from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.BigIntegerField()


    def __str__(self):
        return self.name