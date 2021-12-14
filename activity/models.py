from django.db import models
from django.contrib.auth.models import User




class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField()
    activity = models.CharField(max_length=255)
    file = models.FileField(upload_to='activity/file/', blank=True, null=True)

    def __str__(self):
        return self.name