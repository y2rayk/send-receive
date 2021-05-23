from django.db import models
from django.conf import settings


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='sender')
    text = models.CharField(max_length=200)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='receiver')
    seen = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
