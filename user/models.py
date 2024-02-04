from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    STATUS = [
        ('active', 'Active'),
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    country = CountryField(blank_label="(select country)", null=True, blank=True)
    phonenumber = models.CharField(max_length=25)
    image = models.ImageField(upload_to='user_photos/', null=True, blank = True)
    status = models.CharField(max_length=6, choices = STATUS, default='user')
    created = models.DateTimeField(auto_now_add=True, null=True, blank = True)    
    def __str__(self):
        return self.username


class Yuridik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'Yuridik_User')
    company = models.CharField(max_length=255, verbose_name="company name")
    company_boss = models.CharField(max_length=255, verbose_name = "company boss full name")
    company_certificat = models.FileField(upload_to = 'yuridik_files/', verbose_name = 'company certificat', null = True, blank = True)
    certificat_period = models.IntegerField(validators=[MinValueValidator(2024), MaxValueValidator(2030)], blank = True, null = True)
    company_address = models.CharField(max_length=255, verbose_name="company country, region, city, postal code")

class Jismoniy_Shaxs(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Jismoniy_User")

    JINS = [
            ('male', 'Male'),
            ('female', 'Female'),
        ]

    gender = models.CharField(max_length=6, choices = JINS, null = True)


    