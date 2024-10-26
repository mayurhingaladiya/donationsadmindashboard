from django.db import models
from datetime import date

class Contributor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Charity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Donation(models.Model):
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateField(null=True)