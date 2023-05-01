from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    MALE = "H"
    FEMALE = "F"
    OTHERS = "O"
    GENDER = [
        (MALE, "Homme"),
        (FEMALE, "Femme"),
        (OTHERS, "Autres"),
    ]
    age = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=10,unique=False, null=True,blank=True)
    gender=models.CharField(
        choices=GENDER,
        default=OTHERS, null=False,
    )
    city = models.CharField(max_length=100, null=True)