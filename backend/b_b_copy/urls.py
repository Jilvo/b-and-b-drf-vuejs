"""
URL configuration for b_b_copy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import include, path

from listings.views import LodgementViewSet, Lodgement_Review_RatingsViewSet
from tchats_service.views import ConversationViewSet
from review.views import Lodgement_ReviewViewSet
from bookings.views import BookingViewSet

router = DefaultRouter()
router.register(r"lodgement", LodgementViewSet, basename="lodgement")
router.register(
    r"lodgement_review_ratings",
    Lodgement_Review_RatingsViewSet,
    basename="lodgement_review_ratings",
)
router.register(r"bookings", BookingViewSet, basename="bookings")
router.register(r"conversation", ConversationViewSet, basename="conversation")
router.register(r"lodgement_review", Lodgement_ReviewViewSet, basename="lodgement_review")
urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
]
