# Generated by Django 3.2.4 on 2021-10-06 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211003_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='myfile',
            field=models.ImageField(default='', upload_to='static/profile'),
        ),
    ]