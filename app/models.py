from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

SEX_CHOICES = [
    ('мужской', 'male, мужской, masculino'),  # male, female, other
    ('женский', 'female, женский, femenino'),
    ('другой', 'other, другой, otro')
]
EDU_CHOICES = [
    ('да', 'yes, да, si'),
    ('нет', 'no, нет, no'),
]

COU_CHOICES = [
    ('Algeria', 'Algeria'),
    ('Argentina', 'Argentina'),
    ('Armenia', 'Armenia'),
    ('Australia', 'Australia'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Belarus', 'Belarus'),
    ('Belgium', 'Belgium'),
    ('Brazil', 'Brazil'),
    ('Bulgaria', 'Bulgaria'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Croatia', 'Croatia'),
    ('Czech Republic', 'Czech Republic'),
    ('Estonia', 'Estonia'),
    ('Finland', 'Finland'),
    ('France', 'France'),
    ('Germany', 'Germany'),
    ('India', 'India'),
    ('Iran', 'Iran'),
    ('Italy', 'Italy'),
    ('Japan', 'Japan'),
    ('Korea', 'Korea'),
    ('Latvia', 'Latvia'),
    ('Mexico', 'Mexico'),
    ('Namibia', 'Namibia'),
    ('Nigeria', 'Nigeria'),
    ('Oman', 'Oman'),
    ('Pakistan', 'Pakistan'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Philippines', 'Philippines'),
    ('Russia', 'Russia'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Serbia', 'Serbia'),
    ('Singapore', 'Singapore'),
    ('Slovakia', 'Slovakia'),
    ('Slovenia', 'Slovenia'),
    ('Spain', 'Spain'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Thailand', 'Thailand'),
    ('Tunis', 'Tunis'),
    ('Turkey', 'Turkey'),
    ('United Kingdom ', 'United Kingdom'),
    ('USA', 'USA'),
    ('Other', 'Other'),
]


class Client_Color1(models.Model):
    Client_id = models.AutoField(primary_key=True)
    Client_Year = models.IntegerField(validators=[MinValueValidator(1940), MaxValueValidator(2020)])
    Client_sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    Client_country1 = models.CharField(max_length=50, choices=COU_CHOICES)
    Client_country2 = models.CharField(max_length=50, choices=COU_CHOICES)
    Client_lang = models.CharField(max_length=50)
    Client_edu = models.CharField(max_length=10, choices=EDU_CHOICES)
    Client_shade = models.CharField(max_length=10, choices=EDU_CHOICES)
    color1 = models.CharField(max_length=50)
    color2 = models.CharField(max_length=20)
    color3 = models.CharField(max_length=20)
    color4 = models.CharField(max_length=20)
    color5 = models.CharField(max_length=20)
    left1 = models.CharField(max_length=20)
    left2 = models.CharField(max_length=20)
    left3 = models.CharField(max_length=20)
    left4 = models.CharField(max_length=20)
    left5 = models.CharField(max_length=20)
    left6 = models.CharField(max_length=20)
    left7 = models.CharField(max_length=20)
    left8 = models.CharField(max_length=20)
    left9 = models.CharField(max_length=20)
    left10 = models.CharField(max_length=24)
