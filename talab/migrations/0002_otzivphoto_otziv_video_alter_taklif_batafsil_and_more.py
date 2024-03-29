# Generated by Django 5.0.1 on 2024-02-05 10:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtzivPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='otziv_photos/')),
            ],
        ),
        migrations.AddField(
            model_name='otziv',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='otziv_files/'),
        ),
        migrations.AlterField(
            model_name='taklif',
            name='batafsil',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='taklif',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='otziv',
            name='photo',
            field=models.ManyToManyField(related_name='otziv_photo', to='talab.otzivphoto'),
        ),
    ]
