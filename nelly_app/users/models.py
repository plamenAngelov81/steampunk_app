from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from Core.validators import Validators


class UserProfile(AbstractUser):
    USER_NAME_MAX_LEN = 35
    USER_NAME_MIN_LEN = 5
    PASSWORD_MAX_LEN = 25
    PASSWORD_MIN_LEN = 8
    AGE_MIN_VALUE = 18
    FIRST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 3
    LAST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 3
    PHONE_MIN_LEN = 10
    PHONE_MAX_LEN = 30

    username = models.CharField(
        verbose_name='Username',
        max_length=USER_NAME_MAX_LEN,
        null=False,
        blank=False,
        validators=[MinLengthValidator(USER_NAME_MIN_LEN)],
        unique=True
    )

    first_name = models.CharField(
        verbose_name='First Name',
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
        validators=[MinLengthValidator(FIRST_NAME_MIN_LEN)]
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
        validators=[MinLengthValidator(LAST_NAME_MIN_LEN)]
    )

    age = models.IntegerField(
        verbose_name="Age",
        null=True,
        blank=True,
        validators=[MinValueValidator(AGE_MIN_VALUE)]
    )

    image_url = models.URLField(
        verbose_name='Image URL',
        null=True,
        blank=True
    )

    phone_number = models.CharField(
        verbose_name='Phone Number',
        max_length=PASSWORD_MAX_LEN,
        null=True,
        blank=True,
        validators=[MinLengthValidator(PHONE_MIN_LEN), Validators.phone_num]
    )

    user_address = models.TextField(
        verbose_name='Address',
        null=True,
        blank=True
    )

    @property
    def get_name(self):
        first = ''
        last = ''
        if self.first_name:
            first = self.first_name
        if self.last_name:
            last = self.last_name
        return f"{first} {last}"
