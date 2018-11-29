from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat_model(models.Model):
    conversation = models.CharField(max_length=240)
    username = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "%s: %s" % (self.username, self.conversation) 
