from django.db import models
from django.templatetags.static import static
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        first_name = extra_fields.get('first_name')
        if not first_name:
            raise ValueError('First name must be set.')

        last_name = extra_fields.get('last_name')
        if not last_name:
            raise ValueError('Last name must be set.')

        if not email:
            raise ValueError('E-mail must be set.')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_superuser=extra_fields.get('is_superuser', False),
            is_staff=extra_fields.get('is_staff', False),
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomAuthUser(AbstractUser):
    username = None
    first_name = models.CharField(_("first name"), max_length=150, blank=False, null=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False, null=False)
    email = models.EmailField(_("email address"), blank=False, null=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()


class Profile(models.Model):
    user = models.OneToOneField(CustomAuthUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='users/', null=True, default=None)

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url

        return static('images/default-profile-image.png')
