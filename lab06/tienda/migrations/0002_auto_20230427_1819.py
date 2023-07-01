# Generated by Django 3.2 on 2023-04-27 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='productos/'),
        ),
    ]
