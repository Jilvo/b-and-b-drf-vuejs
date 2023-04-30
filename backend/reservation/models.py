from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# TODO Ajouter les équipements


class Location_Place(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=False, null=False)
    number_of_places = models.IntegerField()
    number_of_bedrooms = models.IntegerField()
    number_of_beds = models.IntegerField()
    number_of_bathrooms = models.IntegerField()
    description = models.CharField(max_length=1000, null=True)
    price = models.IntegerField()

    class Meta:
        verbose_name = "Location Place"
        verbose_name_plural = "Location Places"


class Location_Review_Ratings(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000, null=True)
    general_grade = models.IntegerField()
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Location Review Rating"
        verbose_name_plural = "Location Review Ratings"
