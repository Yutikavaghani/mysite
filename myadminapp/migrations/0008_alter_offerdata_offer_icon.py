# Generated by Django 5.0.1 on 2024-05-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadminapp', '0007_offerdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerdata',
            name='offer_icon',
            field=models.ImageField(blank=True, null=True, upload_to='slider-media/'),
        ),
    ]
