# Generated by Django 5.0.2 on 2024-02-29 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exibition', '0002_alter_sponsor_options_remove_owner_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='phone',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
