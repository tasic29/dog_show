# Generated by Django 5.0.2 on 2024-02-29 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exibition', '0003_alter_owner_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='exibition/images'),
        ),
    ]
