from django.db import models
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Photo(models.Model):
    Image = models.ImageField(upload_to = 'talab_photos', verbose_name='maxsulot photo')


class Tag(models.Model):
    Tag = models.TextField(verbose_name='tag')


class Talab(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='talab_users')
    photo = models.ManyToManyField(Photo, related_name='talab_photo', null=True, blank=True)
    video = models.FileField(upload_to = 'talab_files', null=True, blank=True)
    title = models.CharField(max_length=255)
    batafsil = models.TextField(max_length=255, blank=True, null=True, verbose_name='batafsil')
    min_price = models.IntegerField(validators=[MinValueValidator(0)], verbose_name = 'necha puldan boshlansin')
    max_price = models.IntegerField(validators=[MinValueValidator(0)], verbose_name = 'necha pulgacha bo\'lsin')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CommentPhoto(models.Model):
    image = models.ImageField(upload_to = 'comment_photos', verbose_name='maxsulot photo')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='comment_users')
    talab = models.ForeignKey(Talab, on_delete = models.CASCADE)
    comment = models.TextField(verbose_name='comment')
    photo = models.ManyToManyField(CommentPhoto, related_name = 'Comment_Photo', null=True, blank=True)
    video = models.FileField(upload_to = 'comment_files', null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
    

