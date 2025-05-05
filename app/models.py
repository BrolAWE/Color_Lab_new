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
    ('', ''),
    ('Algeria', 'Algeria'),
    ('Argentina', 'Argentina'),
    ('Armenia', 'Armenia'),
    ('Australia', 'Australia'),
    ('Austria', 'Austria'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Bangladesh', 'Bangladesh'),
    ('Belarus', 'Belarus'),
    ('Belgium', 'Belgium'),
    ('Bolivia', 'Bolivia'),
    ('Brazil', 'Brazil'),
    ('Bulgaria', 'Bulgaria'),
    ('Canada', 'Canada'),
    ('Chile', 'Chile'),
    ('China', 'China'),
    ('Colombia', 'Colombia'),
    ('Croatia', 'Croatia'),
    ('Cyprus', 'Cyprus'),
    ('Czech Republic', 'Czech Republic'),
    ('Denmark', 'Denmark'),
    ('Egypt', 'Egypt'),
    ('Estonia', 'Estonia'),
    ('Finland', 'Finland'),
    ('France', 'France'),
    ('Gabon', 'Gabon'),
    ('Georgia', 'Georgia'),
    ('Germany', 'Germany'),
    ('Greece', 'Greece'),
    ('Haiti', 'Haiti'),
    ('Iceland', 'Iceland'),
    ('India', 'India'),
    ('Indonesia', 'Indonesia'),
    ('Iran', 'Iran'),
    ('Italy', 'Italy'),
    ('Japan', 'Japan'),
    ('Jordan', 'Jordan'),
    ('Kazakhstan', 'Kazakhstan'),
    ('Kenya', 'Kenya'),
    ('Latvia', 'Latvia'),
    ('Mali', 'Mali'),
    ('Mexico', 'Mexico'),
    ('Mongolia', 'Mongolia'),
    ('Namibia', 'Namibia'),
    ('Nepal', 'Nepal'),
    ('Netherlands', 'Netherlands'),
    ('New Zealand', 'New Zealand'),
    ('Norway', 'Norway'),
    ('Nigeria', 'Nigeria'),
    ('Oman', 'Oman'),
    ('Pakistan', 'Pakistan'),
    ('Peru', 'Peru'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Philippines', 'Philippines'),
    ('Republic of Korea', 'Republic of Korea'),
    ('Romania', 'Romania'),
    ('Russia', 'Russia'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Serbia', 'Serbia'),
    ('Senegal', 'Senegal'),
    ('Singapore', 'Singapore'),
    ('Slovakia', 'Slovakia'),
    ('Slovenia', 'Slovenia'),
    ('Spain', 'Spain'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Tadjikistan', 'Tadjikistan'),
    ('Taiwan', 'Taiwan'),
    ('Thailand', 'Thailand'),
    ('Togo', 'Togo'),
    ('Tunis', 'Tunis'),
    ('Turkey', 'Turkey'),
    ('United Kingdom ', 'United Kingdom'),
    ('UAE', 'UAE'),
    ('UK', 'UK'),
    ('USA', 'USA'),
    ('Zimbabwe', 'Zimbabwe'),
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
