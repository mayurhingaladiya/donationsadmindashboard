from django.db import models
from datetime import date

class Contributor(models.Model):
    """ Contributor model """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    member = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Charity(models.Model):
    """ Charity model """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Donation(models.Model):
    """ Donation model """
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date = models.DateField(null=True)