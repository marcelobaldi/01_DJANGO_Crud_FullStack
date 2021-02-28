from django.db import models

class Custumer(models.Model):
    name  = models.CharField(max_length=255)
    age   = models.IntegerField()
    email = models.CharField(max_length=255)
    passw = models.CharField(max_length=255)

    def __str__(self):
        return self.email




