from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length = 140)
    last_name = models.CharField(max_length = 140)
    random_number = models.IntegerField(default=0, blank=True, null=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.random_number})"
