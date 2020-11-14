from django.db import models

# Create your models here.

class Device(models.Model):
    type   = models.CharField(max_length=100, blank=False)
    price  = models.IntegerField()
    choices = (
        ('Available','Item Ready to purches'),
        ('Sold','Item Sold out already'),
        ('Restoking','Item restocking for few days')

    )
    status = models.CharField(max_length=50, choices=choices,default="Sold")
    issue  = models.CharField(max_length=50, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.type} , Price {self.price}'

class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass
    