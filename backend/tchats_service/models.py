from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser

from listings.models import Lodgement


# Create your models here.
class Conversation(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL)
    lodgement = models.ForeignKey(Lodgement, on_delete=models.CASCADE, null=False)


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="messages"
    )
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
