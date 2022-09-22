# Generated by Django 3.2.4 on 2022-09-22 16:05

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='email',
            field=models.EmailField(default='mail@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(default='name', max_length=255),
        ),
        migrations.AddField(
            model_name='message',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
        migrations.AddField(
            model_name='message',
            name='surname',
            field=models.CharField(default='surname', max_length=255),
        ),
    ]