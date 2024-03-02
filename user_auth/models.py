from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from common.models import BaseModel
from user_auth.utils import create_token


class UserProfile(BaseModel, AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        db_column="username",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    password = models.CharField(db_column="password", max_length=128)
    first_name = models.CharField(db_column="first_name", max_length=150)
    last_name = models.CharField(db_column="last_name", max_length=150)

    @staticmethod
    def exist_username(username):
        """checking username exists"""
        user = UserProfile.objects.filter(username__iexact=username).first()
        return user

    def get_token(self):
        return create_token(self)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user_profile"
        indexes = [
            models.Index(fields=["username"], name="username_idx"),
        ]
