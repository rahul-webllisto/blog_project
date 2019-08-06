from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, User
)
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email=None, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        # import pdb; pdb.set_trace()
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_staffuser(
            email=email,
            password=password,
        )
        user.email = email
        
        user.is_staff = True
        user.is_admin = True
        user.role = 'admin'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
        null=False, blank=False
    )       
    is_active = models.BooleanField(default=True)    
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return str(self.email)

    # def get_full_name(self):
    #     '''
    #     Returns the first_name plus the last_name, with a space in between.
    #     '''
    #     return self.full_name

    # def get_short_name(self):
    #     '''
    #     Returns the short name for the user.
    #     '''
    #     return self.full_name

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
