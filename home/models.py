from django.db import models

class UzAuto(models.Model):
    nomi = models.CharField(max_length=225)
    rangi = models.CharField(max_length=225)
    narxi = models.CharField(max_length=225)

    def __str__(self):
        return self.nomi
