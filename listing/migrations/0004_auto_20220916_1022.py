# Generated by Django 3.2.4 on 2022-09-16 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0003_auto_20220914_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image_eight',
            field=models.ImageField(default='../default_post_kqniyi.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_five',
            field=models.ImageField(default='../default_post_kqniyi.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_four',
            field=models.ImageField(default='../default_post_kqniyi.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_one',
            field=models.ImageField(default='../default_post_kqniyi.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_seven',
            field=models.ImageField(default='../default_post_kqniyi.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_six',
            field=models.ImageField(default='../default_post_kqniyi.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_three',
            field=models.ImageField(default='../default_post_kqniyi.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='image_two',
            field=models.ImageField(default='../default_post_kqniyi.jpg', upload_to='images/'),
        ),
    ]
