# Generated by Django 5.0.2 on 2024-02-29 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exibition', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='owner',
            name='email',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='last_name',
        ),
    ]