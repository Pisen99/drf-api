# Generated by Django 3.2.18 on 2023-03-09 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../default_profile_yktfo7', upload_to='images/'),
        ),
    ]
