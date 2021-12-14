from django.db import models
from django.contrib.auth.models import User



class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username + ' | ' + self.skill
