from django.conf import settings
from django.contrib import admin
from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.PositiveSmallIntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Breed(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Dog(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    weight = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=255)
    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, related_name='dogs')
    breed = models.ForeignKey(
        Breed, on_delete=models.PROTECT, related_name='dogs_breed')

    def __str__(self) -> str:
        return f'{self.breed} - {self.name}'


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_email = models.EmailField(unique=True)
    contact_phone = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    sponsor = models.ForeignKey(
        Sponsor, on_delete=models.SET_NULL, null=True, related_name='shows')

    def __str__(self) -> str:
        return f'{self.name} - {self.location}'


class Judge(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
