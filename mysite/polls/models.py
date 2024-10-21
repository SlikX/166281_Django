import datetime
from django.utils import timezone

from django.db import models

# Create your models here.

# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

GENDERS = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=60)
    opis = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.nazwa

class Osoba(models.Model):
    class Plec(models.IntegerChoices):
        FEMALE = 1, 'Kobieta'
        MALE = 2, 'Mężczyzna'
        OTHER = 3, 'Inne'

    GENDERS = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=60)
    # plec = models.CharField(max_length=10, choices=GENDERS, default=GENDERS[0][0])
    plec = models.IntegerField(choices=Plec.choices, null=False, blank=False)
    stanowisko = models.ForeignKey(Stanowisko, null=True, blank=True, on_delete=models.SET_NULL)
    data_dodania = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nazwisko']
        unique_together = (('imie', 'nazwisko'),)


    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)