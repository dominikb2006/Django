from django.db import models


class User(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return str(self.FirstName + " " + self.LastName)
