from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database nodel for users in the system
    По умолчанию Django имеет реализованный функционал создания пользователей,
    но его можно переопределить за счет создания своего класса в models.py,
    как только мы свой созданный пустой класс наследуем от AbstractBaseUser и PermissionsMixin,
    то весь базовый функционал создания пользователей появляется в нашем пустом классе,
    а далее добавлением новых полей и переопределением необходимых полей мы кастомизируем
    создание пользователей под свои нужды.

    Метод __str__ необходимо переопределять, чтобы было нормальное
    текстовое представление экземпляров модели в админке и консоли.
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' # username
    REQUIRED_FIELDS = ['name']

    def get_fuul_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email