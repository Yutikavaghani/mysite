# Generated by Django 5.0.1 on 2024-04-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadminapp', '0003_filedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='filedata',
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]
