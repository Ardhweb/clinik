from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

# Choices for the role field
user_type = (
    ('doctor', 'Doctor'),
    ('patient', 'Patient'),
)

class User(AbstractUser):
    username = models.CharField(max_length=255,blank=False, unique=True)    
    #name = models.CharField(max_length=20,null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=20,choices=user_type, default='user',)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = CustomUserManager()

    '''class Meta:
        db_table = 'users' '''

    def __str__(self):
        return self.username

class Address(models.Model):
    line1 = models.CharField(max_length=255,blank=False, null=True)
    city = models.CharField(max_length=255,blank=False, null=True)
    state = models.CharField(max_length=255,blank=False, null=True)
    pincode = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.pincode}"
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  null=True)
    image = models.ImageField(upload_to='profile_pic/')
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)






