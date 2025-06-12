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
    ('Ghana', 'Ghana'),
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
    ('Malaysia', 'Malaysia'),
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

REG_CHOICES = [
    ('', ''),
    ('Алтайский край', 'Алтайский край'),
    ('Амурская область', 'Амурская область'),
    ('Архангельская область', 'Архангельская область'),
    ('Астраханская область', 'Астраханская область'),
    ('Белгородская область', 'Белгородская область'),
    ('Брянская область', 'Брянская область'),
    ('Владимирская область', 'Владимирская область'),
    ('Волгоградская область', 'Волгоградская область'),
    ('Вологодская область', 'Вологодская область'),
    ('Воронежская область', 'Воронежская область'),
    ('г. Москва', 'г. Москва'),
    ('г. Санкт-Петербург', 'г. Санкт-Петербург'),
    ('г. Севастополь', 'г. Севастополь'),
    ('Донецкая Народная Республика', 'Донецкая Народная Республика'),
    ('Еврейская автономная область', 'Еврейская автономная область'),
    ('Забайкальский край', 'Забайкальский край'),
    ('Запорожская область', 'Запорожская область'),
    ('Ивановская область', 'Ивановская область'),
    ('Иркутская область', 'Иркутская область'),
    ('Кабардино-Балкарская Республика', 'Кабардино-Балкарская Республика'),
    ('Калининградская область', 'Калининградская область'),
    ('Калужская область', 'Калужская область'),
    ('Камчатский край', 'Камчатский край'),
    ('Карачаево-Черкесская Республика', 'Карачаево-Черкесская Республика'),
    ('Кемеровская область', 'Кемеровская область'),
    ('Кировская область', 'Кировская область'),
    ('Костромская область', 'Костромская область'),
    ('Краснодарский край', 'Краснодарский край'),
    ('Красноярский край', 'Красноярский край'),
    ('Курганская область', 'Курганская область'),
    ('Курская область', 'Курская область'),
    ('Ленинградская область', 'Ленинградская область'),
    ('Липецкая область', 'Липецкая область'),
    ('Луганская Народная Республика', 'Луганская Народная Республика'),
    ('Магаданская область', 'Магаданская область'),
    ('Московская область', 'Московская область'),
    ('Мурманская область', 'Мурманская область'),
    ('Ненецкий автономный округ', 'Ненецкий автономный округ'),
    ('Нижегородская область', 'Нижегородская область'),
    ('Новгородская область', 'Новгородская область'),
    ('Новосибирская область', 'Новосибирская область'),
    ('Омская область', 'Омская область'),
    ('Оренбургская область', 'Оренбургская область'),
    ('Орловская область', 'Орловская область'),
    ('Пензенская область', 'Пензенская область'),
    ('Пермский край', 'Пермский край'),
    ('Приморский край', 'Приморский край'),
    ('Псковская область', 'Псковская область'),
    ('Республика Адыгея', 'Республика Адыгея'),
    ('Республика Алтай', 'Республика Алтай'),
    ('Республика Башкортостан', 'Республика Башкортостан'),
    ('Республика Бурятия', 'Республика Бурятия'),
    ('Республика Дагестан', 'Республика Дагестан'),
    ('Республика Ингушетия', 'Республика Ингушетия'),
    ('Республика Калмыкия', 'Республика Калмыкия'),
    ('Республика Карелия', 'Республика Карелия'),
    ('Республика Коми', 'Республика Коми'),
    ('Республика Крым', 'Республика Крым'),
    ('Республика Марий Эл', 'Республика Марий Эл'),
    ('Республика Мордовия', 'Республика Мордовия'),
    ('Республика Саха (Якутия)', 'Республика Саха (Якутия)'),
    ('Республика Северная Осетия - Алания', 'Республика Северная Осетия - Алания'),
    ('Республика Татарстан (Татарстан)', 'Республика Татарстан (Татарстан)'),
    ('Республика Тыва', 'Республика Тыва'),
    ('Республика Хакасия', 'Республика Хакасия'),
    ('Ростовская область', 'Ростовская область'),
    ('Рязанская область', 'Рязанская область'),
    ('Самарская область', 'Самарская область'),
    ('Саратовская область', 'Саратовская область'),
    ('Сахалинская область', 'Сахалинская область'),
    ('Свердловская область', 'Свердловская область'),
    ('Смоленская область', 'Смоленская область'),
    ('Ставропольский край', 'Ставропольский край'),
    ('Тамбовская область', 'Тамбовская область'),
    ('Тверская область', 'Тверская область'),
    ('Томская область', 'Томская область'),
    ('Тульская область', 'Тульская область'),
    ('Тюменская область', 'Тюменская область'),
    ('Удмуртская Республика', 'Удмуртская Республика'),
    ('Ульяновская область', 'Ульяновская область'),
    ('Хабаровский край', 'Хабаровский край'),
    ('Ханты-Мансийский АО - Югра', 'Ханты-Мансийский АО - Югра'),
    ('Херсонская область', 'Херсонская область'),
    ('Челябинская область', 'Челябинская область'),
    ('Чеченская Республика', 'Чеченская Республика'),
    ('Чувашская Республика - Чувашия', 'Чувашская Республика - Чувашия'),
    ('Чукотский автономный округ', 'Чукотский автономный округ'),
    ('Ямало-Ненецкий автономный округ', 'Ямало-Ненецкий автономный округ'),
    ('Ярославская область', 'Ярославская область'),
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


class Client_Color2(models.Model):
    Client_id = models.AutoField(primary_key=True)
    Client_Year = models.IntegerField(validators=[MinValueValidator(1940), MaxValueValidator(2020)])
    Client_sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    Client_region = models.CharField(max_length=50, choices=REG_CHOICES)
    Client_edu = models.CharField(max_length=10, choices=EDU_CHOICES)
    Client_shade = models.CharField(max_length=10, choices=EDU_CHOICES)
    color_like = models.CharField(max_length=20, default='')
    color_dislike = models.CharField(max_length=20, default='')
    color1 = models.CharField(max_length=20, default='')
    color2 = models.CharField(max_length=20, default='')
    color3 = models.CharField(max_length=20, default='')
    color4 = models.CharField(max_length=20, default='')
    color5 = models.CharField(max_length=20, default='')
    left1 = models.CharField(max_length=20, default='')
    left2 = models.CharField(max_length=20, default='')
    left3 = models.CharField(max_length=20, default='')
    left4 = models.CharField(max_length=20, default='')
    left5 = models.CharField(max_length=20, default='')
    left6 = models.CharField(max_length=20, default='')
    left7 = models.CharField(max_length=20, default='')
    left8 = models.CharField(max_length=20, default='')
    left9 = models.CharField(max_length=20, default='')
    left10 = models.CharField(max_length=20, default='')
