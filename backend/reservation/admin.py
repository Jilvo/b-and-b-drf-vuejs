from django.contrib import admin

from reservation.models import Location_Place, Location_Review_Ratings

# Register your models here.
admin.site.register(Location_Place)
admin.site.register(Location_Review_Ratings)
