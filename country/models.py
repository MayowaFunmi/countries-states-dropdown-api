from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Country(models.Model):
    alpha_2 = models.CharField(max_length=5)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f' {self.country.alpha_2} ({self.country.name})'


class Person(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name.first_name} {self.name.last_name}'


class NigeriaStates(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class LocalGovernmentArea(models.Model):
    state = models.ForeignKey(NigeriaStates, on_delete=models.CASCADE, related_name='local_govt')
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name} in {self.state.name}'


class LocalGovernmentDropdown(models.Model):
    state = models.ForeignKey(NigeriaStates, on_delete=models.CASCADE)
    local_govt_area = models.ForeignKey(LocalGovernmentArea, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.local_govt_area} in {self.state.name}'
