from django.contrib.auth.models import User, AbstractUser
from django.db import models


class TimeStamped(models.Model):
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)


class ServiceType(TimeStamped):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    extra_data = models.JSONField(default=dict)


class Discount(models.Model):
    """
    Discount applicable to the price of a service or product
    """
    name = models.CharField(max_length=255, default="Sconto Generico")
    discount_percentage = models.FloatField(help_text="sconto")


class Cost(models.Model):
    unit_of_measure = models.CharField(choices=((('m','metro'), ('cm', 'centimetro'), ('kg', 'chilo'), ('pz','pezzi'))), default='metro',
        max_length=255, help_text="unita` di misura per il prezzo (metri, pezzi, centimetri)")
    price = models.FloatField(help_text="prezzo all'unita` di misura")
    discount = models.ForeignKey(Discount, on_delete=models.PROTECT)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.ForeignKey(Cost, on_delete=models.PROTECT)
    discount = models.ForeignKey(Discount, on_delete=models.PROTECT)

#
# class Customer(AbstractUser):
#     """"""
#     user_type = "Customer"

#
# class Employee(AbstractUser):
#     perm_type = models.CharField(max_length=255)