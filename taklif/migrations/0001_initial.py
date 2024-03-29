# Generated by Django 5.0.1 on 2024-02-05 10:30

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='comment_photos', verbose_name='maxsulot photo')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='talab_photos', verbose_name='maxsulot photo')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag', models.TextField(verbose_name='tag')),
            ],
        ),
        migrations.CreateModel(
            name='Talab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='talab_files')),
                ('title', models.CharField(max_length=255)),
                ('batafsil', models.TextField(blank=True, max_length=255, null=True, verbose_name='batafsil')),
                ('min_price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='necha puldan boshlansin')),
                ('max_price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name="necha pulgacha bo'lsin")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talab_users', to=settings.AUTH_USER_MODEL)),
                ('photo', models.ManyToManyField(blank=True, null=True, related_name='talab_photo', to='taklif.photo')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='comment')),
                ('video', models.FileField(blank=True, null=True, upload_to='comment_files')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_users', to=settings.AUTH_USER_MODEL)),
                ('photo', models.ManyToManyField(blank=True, null=True, related_name='Comment_Photo', to='taklif.commentphoto')),
                ('talab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taklif.talab')),
            ],
        ),
    ]
