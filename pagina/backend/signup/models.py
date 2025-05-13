from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    run = models.CharField(max_length=12, unique=True)  # Campo para almacenar el RUN
    


    def __str__(self):
        return self.user.username
