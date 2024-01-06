from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone 
import jwt


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    photo = models.FileField(upload_to="users/", blank=True)
    token = models.TextField(blank=True)
    token_renewed = models.DateTimeField(default=None, null=True, blank=True)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    def set_token(self) -> str:
        encoded_token = jwt.encode({"id": self.id}, settings.SECRET_KEY, algorithm="HS256")
        self.token = encoded_token
        self.token_renewed = timezone.localtime()
        self.save(update_fields=["token", "token_renewed"])
        return encoded_token
