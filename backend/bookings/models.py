from django.db import models
from django.conf import settings
from django.contrib.auth.models import User,AbstractUser
from django.forms import ValidationError

from listings.models import Lodgement


# Create your models here.

class Booking(models.Model):
    lodgement = models.ForeignKey(Lodgement, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError("End date must be after start date")

    def is_available(self, start_date, end_date):
        overlapping_bookings = self.booking_set.filter(
            start_date__lt=end_date,
            end_date__gt=start_date,
        )
        return not overlapping_bookings.exists()
    def __str__(self):
        return f'Booking at {self.lodgement} by {self.user} from {self.start_date} to {self.end_date}'
