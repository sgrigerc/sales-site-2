# Generated by Django 3.2.15 on 2022-10-24 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to='profile_images'),
        ),
    ]