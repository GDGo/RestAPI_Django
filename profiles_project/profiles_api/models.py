from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for User profiles
    Переопределение менеджера требуется для того, чтобы Django знала как создавать пользователей и
    суперпользователей на основе нашего собственного класса UserProfile, который имеет кастомное поле
    email, являющееся полем username.

    В стандартной реализации класса для пользователй в качестве username выступает
    поле с таким же названием username
    """

    def create_user(self, email, name, password=None):
        """Create a new User profile
        Пароль опционален, но если он не будет указываться при создании пользователя,
        то он не сможет аутентифицироваться, это необходимо например когда требуется сменить
        пароль при первом входе
        """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        """По Умолчанию self.model ссылается на модель для которой этот менеджер предназначен
        т.е. на модель UserProfile и тем самы создается новый экземпляр модели UserProfile и в него 
        передаются параметры email=email, naem=name"""
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


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