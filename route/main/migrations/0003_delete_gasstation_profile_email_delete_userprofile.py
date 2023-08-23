# Generated by Django 4.2.4 on 2023-08-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_profile_first_name_remove_profile_last_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GasStation',
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='Email'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
