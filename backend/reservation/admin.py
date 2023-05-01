from django.contrib import admin

from reservation.models import Lodgement, Lodgement_Review_Ratings

# Register your models here.
admin.site.register(Lodgement)
admin.site.register(Lodgement_Review_Ratings)
