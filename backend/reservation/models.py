from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,AbstractUser


# Create your models here.
# TODO Ajouter les équipements
# TODO ajouter last connection



class Lodgement(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=False, null=False)
    number_of_places = models.IntegerField()
    number_of_bedrooms = models.IntegerField()
    number_of_beds = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    description = models.CharField(max_length=1000, null=True)
    price = models.IntegerField()

    class Meta:
        verbose_name = "Lodgement Place"
        verbose_name_plural = "Lodgement Places"


class Lodgement_Review_Ratings(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000, null=True)
    general_grade = models.IntegerField()
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Lodgement Review Rating"
        verbose_name_plural = "Lodgement Review Ratings"
