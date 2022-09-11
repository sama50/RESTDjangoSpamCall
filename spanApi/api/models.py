from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phone_field import PhoneField

class MyUserManager(BaseUserManager):
    def create_user(self, phone, name,password=None,password2=None,email=None):
         
        if not phone:
            raise ValueError('Users must have an email address')

        user = self.model(
            phone=self.normalize_email(phone),
            name=name,
            email=email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, name, password=None):
         
        user = self.create_user(
            phone,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone = models.CharField(max_length=14,unique=True)

    # date_of_birth = models.DateField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
        

class spanNumber(models.Model):
    number = models.CharField(max_length=15,unique=True)
    name = models.CharField(max_length=20,default=None)