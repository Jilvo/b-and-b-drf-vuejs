from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,AbstractUser


# Create your models here.
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

class Bathroom_Lodgement_Equipment(models.Model):
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    bathtub = models.BooleanField(default=False)
    hair_dryer = models.BooleanField(default=False)
    shampoo = models.BooleanField(default=False)
    soap = models.BooleanField(default=False)
    hot_water = models.BooleanField(default=False)
    shower_gel = models.BooleanField(default=False)

class Bedroom_Lodgement_Equipment(models.Model):
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    washing_machine = models.BooleanField(default=False)
    clothes_dryer = models.BooleanField(default=False)
    washing_machine = models.BooleanField(default=False)
    basic_bedroom_equipment = models.BooleanField(default=False)
    hangers = models.BooleanField(default=False)
    sheets = models.BooleanField(default=False)
    pillows = models.BooleanField(default=False)
class Distraction_Lodgement_Equipment(models.Model):
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    television = models.BooleanField(default=False)
    game_console = models.BooleanField(default=False)
    piano = models.BooleanField(default=False)
    bike = models.BooleanField(default=False)

class Family_Lodgement_Equipment(models.Model):
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    high_chair = models.BooleanField(default=False)
    child_dishes = models.BooleanField(default=False)
    child_toys = models.BooleanField(default=False)
    stroller = models.BooleanField(default=False)
    baby_safety_gate = models.BooleanField(default=False)

class Climatisation_Lodgement_Equipment(models.Model):
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    climatisation = models.BooleanField(default=False)
    chimney = models.BooleanField(default=False)
    fan_ceiling = models.BooleanField(default=False)
    heating = models.BooleanField(default=False)

class Home_Security_Lodgement_Equipment(models.Model):
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    smoke_detector = models.BooleanField(default=False)
    first_aid_kit = models.BooleanField(default=False)
    extinctor = models.BooleanField(default=False)

class Internet_Lodgement_Equipment(models.Model):
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    wifi_presence = models.BooleanField(default=False)
    work_space_presence = models.BooleanField(default=False)

class Kitchen_Logdment_Equipment(models.Model):
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    kitchen_presence = models.BooleanField(default=False)
    fridge = models.BooleanField(default=False)
    oven = models.BooleanField(default=False)
    basic_kitchen_equipment = models.BooleanField(default=False)
    dishes = models.BooleanField(default=False)
    dishwasher = models.BooleanField(default=False)
    coffee_maker = models.BooleanField(default=False)
    hob = models.BooleanField(default=False)

class Exterior_Lodgement_Equipment(models.Model):
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    balcony = models.BooleanField(default=False)
    barbecue = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)

class Parking_Lodgement_Equipment(models.Model):
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    parking_in_the_lodgement = models.BooleanField(default=False)
    parking_in_the_street = models.BooleanField(default=False)

class Services_Lodgement(models.Model):
    lodgement_id = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    animals_accepted = models.BooleanField(default=False)
    smoker_lodgement = models.BooleanField(default=False)
    key_gaven_by_the_host = models.BooleanField(default=False)
    secured_key_box= models.BooleanField(default=False)
    autonomous_arrival = models.BooleanField(default=False)
