from django.db import models


class Message(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
