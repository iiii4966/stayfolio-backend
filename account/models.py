from django.db import models

class Accounts(models.Model):
    name          = models.CharField(max_length=60)
    email         = models.EmailField(max_length=100, unique=True)
    password      = models.CharField(max_length=200, null=True)
    phone_number  = models.CharField(max_length=16, blank=True)
    membership    = models.BooleanField(default=False,null=True)
    profile_image = models.CharField(max_length=4000)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='account'
