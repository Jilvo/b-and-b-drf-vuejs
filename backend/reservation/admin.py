from django.contrib import admin

from reservation.models import (
    Lodgement,
    Lodgement_Review_Ratings,
    Bathroom_Lodgement_Equipment,
    Bedroom_Lodgement_Equipment,
    Distraction_Lodgement_Equipment,
    Family_Lodgement_Equipment,
    Climatisation_Lodgement_Equipment,
    Home_Security_Lodgement_Equipment,
    Internet_Lodgement_Equipment,
    Kitchen_Logdment_Equipment,
    Exterior_Lodgement_Equipment,
    Parking_Lodgement_Equipment,
    Services_Lodgement,
)

# Register your models here.
admin.site.register(Lodgement)
admin.site.register(Lodgement_Review_Ratings)
admin.site.register(Bathroom_Lodgement_Equipment)
admin.site.register(Bedroom_Lodgement_Equipment)
admin.site.register(Distraction_Lodgement_Equipment)
admin.site.register(Family_Lodgement_Equipment)
admin.site.register(Climatisation_Lodgement_Equipment)
admin.site.register(Home_Security_Lodgement_Equipment)
admin.site.register(Internet_Lodgement_Equipment)
admin.site.register(Kitchen_Logdment_Equipment)
admin.site.register(Exterior_Lodgement_Equipment)
admin.site.register(Parking_Lodgement_Equipment)
admin.site.register(Services_Lodgement)
