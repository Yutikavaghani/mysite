# Generated by Django 5.0.1 on 2024-05-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadminapp', '0005_sliderdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliderdata',
            name='background_img',
            field=models.ImageField(upload_to='slider-media/'),
        ),
    ]
