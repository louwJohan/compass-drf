# Generated by Django 3.2.4 on 2022-09-26 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='content',
            new_name='profile_content',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profile_image',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='profile_name',
        ),
    ]
