# Generated by Django 5.0.6 on 2024-07-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryitem',
            name='content',
            field=models.FileField(upload_to='gallery/'),
        ),
    ]
