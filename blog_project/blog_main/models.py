from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile_no = models.CharField(max_length=10)
    address = models.CharField(max_length=60)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Country = models.CharField(max_length=20)
    PinCode = models.CharField(max_length=6)
    Profile_Image = models.ImageField(upload_to='profile_images')
    is_bloger = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)

    def __str__(self):
        return self.username

