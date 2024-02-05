from django.db import models
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Photo(models.Model):
    image = models.ImageField(upload_to='taklif_photos/')


class Tag(models.Model):
    tag = models.TextField()


class Taklif(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    batafsil = models.TextField(max_length=255, null=True, blank=True)
    photo = models.ManyToManyField(Photo, related_name='taklif_photo')
    video = models.FileField(upload_to='taklif_videos/', blank=True, null=True)
    tag = models.ManyToManyField(Tag, related_name='taklif_tag')
    price = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


class OtzivPhoto(models.Model):
    image = models.ImageField(upload_to='otziv_photos/')


class Otziv(models.Model):
    STATUS = [
        ('1','*'),
        ('2','**'),
        ('3','***'),
        ('4','****'),
        ('5','*****'),
    ]
    status = models.CharField(max_length=6, choices=STATUS, default = '5')
    comment = models.TextField(verbose_name = 'Izoh')
    taklif = models.ForeignKey(Taklif, on_delete = models.CASCADE)
    video = models.FileField(upload_to='otziv_files/', blank=True, null=True)
    photo = models.ManyToManyField(OtzivPhoto, related_name='otziv_photo')

    def __str__(self):
        return self.taklif.title


