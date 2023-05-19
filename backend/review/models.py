from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,AbstractUser

from listings.models import Lodgement

# Create your models here.

class Lodgement_Review(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    lodgement = models.ForeignKey(Lodgement, on_delete=models.CASCADE, null=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    review_content = models.CharField(max_length=1000,null=True)
    cleaning_grade = models.IntegerField(choices=RATING_CHOICES,null=False,default=5)
    communication_grade = models.IntegerField(choices=RATING_CHOICES,null=False,default=5)
    localization_grade = models.IntegerField(choices=RATING_CHOICES,null=False,default=5)
    quality_price_ratio_grade = models.IntegerField(choices=RATING_CHOICES,null=False,default=5)

    @property
    def average_grade(self):
        grades = [self.cleaning_grade, self.communication_grade, self.localization_grade, self.quality_price_ratio_grade]
        return sum(grades) / len(grades)