# Generated by Django 5.0.1 on 2024-05-23 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadminapp', '0006_alter_sliderdata_background_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='offerdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_icon', models.ImageField(upload_to='slider-media/')),
                ('offer_heading', models.CharField(max_length=200)),
                ('offer_des', models.CharField(max_length=1000)),
            ],
        ),
    ]
