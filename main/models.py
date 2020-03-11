from django.contrib.auth.models import AbstractUser , User
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_ceo = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_cto = models.BooleanField(default=False)
    is_senior_developer = models.BooleanField(default=False)
    is_junior_developer = models.BooleanField(default=False)


class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title