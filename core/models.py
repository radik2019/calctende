from django.contrib.auth.models import User, AbstractUser
from django.db import models


class TimeStamped(models.Model):
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)

class ServiceType(TimeStamped):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    unit_of_measure = models.CharField(choices=('metro, centimetro, chilo, pezzi'), default='metro',
        max_length=255, help_text="unita` di misura per il prezzo (metri, pezzi, centimetri)")
    price = models.FloatField(help_text="prezzo all'unita` di misura")
    # user = models.ForeignKey(User, "")#User()

class Customer(AbstractUser):
    """"""


class Employee(AbstractUser):
    perm_type = models.CharField(max_length=255)