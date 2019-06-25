from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, User
)
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(
            username=self.normalize_email(username),
        )

        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        # import pdb; pdb.set_trace()
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_staffuser(
            username=username,
            password=password,
        )
        user.username = username
        
        user.is_staff = True
        user.is_admin = True
        user.role = 'admin'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.EmailField(
        max_length=255,
        unique=True,
        null=False, blank=False
    )
    full_name = models.CharField(
        ('full_name'), max_length=256, blank=True, null=True)    
    is_active = models.BooleanField(default=True)    
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return str(self.get_full_name())

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.full_name

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.full_name

    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_staff

    def is_admin(self):
        "Is the user a admin member?"
        return self.is_admin

    def is_active(self):
        "Is the user active?"
        return self.is_active

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
