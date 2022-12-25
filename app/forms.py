from django import forms
from .models import Client_Color1

SEX_CHOICES_EN = [
    ('', ''),
    ('мужской', 'male'),  # male, female, other
    ('женский', 'female'),
    ('другой', 'other')
]

EDU_CHOICES_EN = [
    ('', ''),
    ('да', 'yes'),
    ('нет', 'no'),
]

SEX_CHOICES_RU = [
    ('', ''),
    ('мужской', 'мужской'),  # male, female, other
    ('женский', 'женский'),
    ('другой', 'другой')
]

EDU_CHOICES_RU = [
    ('', ''),
    ('да', 'да'),
    ('нет', 'нет'),
]

SEX_CHOICES_ES = [
    ('', ''),
    ('мужской', 'masculino'),  # male, female, other
    ('женский', 'femenino'),
    ('другой', 'otro')
]

EDU_CHOICES_ES = [
    ('', ''),
    ('да', 'si'),
    ('нет', 'no'),
]

SEX_CHOICES_AR = [
    ('', ''),
    ('мужской', 'ذكر'),  # male, female, other
    ('женский', 'أنثى'),
    ('другой', 'آخر')
]

EDU_CHOICES_AR = [
    ('', ''),
    ('да', 'نعم'),
    ('нет', 'لا'),
]

SEX_CHOICES_CZ = [
    ('', ''),
    ('мужской', 'muž'),  # male, female, other
    ('женский', 'žena'),
    ('другой', 'jiné')
]

EDU_CHOICES_CZ = [
    ('', ''),
    ('да', 'ano'),
    ('нет', 'ne'),
]

COU_CHOICES = [
    ('', ''),
    ('Algeria', 'Algeria'),
    ('Australia', 'Australia'),
    ('Argentina', 'Argentina'),
    ('Armenia', 'Armenia'),
    ('Azerbaijan', 'Azerbaijan'),
    ('Belarus', 'Belarus'),
    ('Brazil', 'Brazil'),
    ('Belgium', 'Belgium'),
    ('Bulgaria', 'Bulgaria'),
    ('Chile', 'Chile'),
    ('Czech Republic', 'Czech Republic'),
    ('China', 'China'),
    ('Croatia', 'Croatia'),
    ('Estonia', 'Estonia'),
    ('Finland', 'Finland'),
    ('France', 'France'),
    ('Germany', 'Germany'),
    ('Italy', 'Italy'),
    ('India', 'India'),
    ('Iran', 'Iran'),
    ('Japan', 'Japan'),
    ('Korea', 'Korea'),
    ('Latvia', 'Latvia'),
    ('Mexico', 'Mexico'),
    ('Nigeria', 'Nigeria'),
    ('Namibia', 'Namibia'),
    ('Poland', 'Poland'),
    ('Portugal', 'Portugal'),
    ('Russia', 'Russia'),
    ('Spain', 'Spain'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Serbia', 'Serbia'),
    ('Singapore', 'Singapore'),
    ('Slovakia', 'Slovakia'),
    ('Slovenia', 'Slovenia'),
    ('Sweden', 'Sweden'),
    ('Switzerland', 'Switzerland'),
    ('Turkey', 'Turkey'),
    ('Thailand', 'Thailand'),
    ('Tunis', 'Tunis'),
    ('United Kingdom ', 'United Kingdom'),
    ('USA', 'USA'),
    ('Other', 'Other'),
]


class Client_ColorForm(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('Год Вашего рождения :'), 'Client_sex': ('Ваш пол :'),
            'Client_country1': ('Страна рождения :'),
            'Client_country2': ('Страна постоянного проживания :'), 'Client_lang': ('Родной язык :'),
            'Client_edu': ('Художественное образование :'),
            'Client_shade': ('Испытываете ли Вы сложности с восприятием каких-либо оттенков?')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Значение слишком длинное"),
                'Client_Year': ("Значение слишком длинное"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_RU
        self.fields['Client_edu'].choices = EDU_CHOICES_RU
        self.fields['Client_shade'].choices = EDU_CHOICES_RU

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='Год Вашего рождения :')


class Client_ColorForm_en(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('Year of birth :'), 'Client_sex': ('Gender :'), 'Client_country1': ('Country of birth :'),
            'Client_country2': ('Country of residence :'), 'Client_lang': ('Mother tongue :'),
            'Client_edu': ('Art education :'),
            'Client_shade': ('Do you have difficulties seeing certain colours?')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Value is too long"),
                'Client_Year': ("Value is too long"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_EN
        self.fields['Client_edu'].choices = EDU_CHOICES_EN
        self.fields['Client_shade'].choices = EDU_CHOICES_EN

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='Year of birth :')


class Client_ColorForm_es(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('Año de nacimiento :'), 'Client_sex': ('Género :'),
            'Client_country1': ('País de nacimiento :'),
            'Client_country2': ('País de residencia :'), 'Client_lang': ('Lengua materna :'),
            'Client_edu': ('Educación artística :'),
            'Client_shade': ('¿Tienes dificultad para ver ciertos colores (por ejemplo, tienes daltonismo)?')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("El valor es demasiado largo"),
                'Client_Year': ("El valor es demasiado largo"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_ES
        self.fields['Client_edu'].choices = EDU_CHOICES_ES
        self.fields['Client_shade'].choices = EDU_CHOICES_ES

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='Año de nacimiento :')


class Client_ColorForm_ar(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': 'تاريخ الميلاد', 'Client_sex': 'النوع', 'Client_country1': 'بلد المولد',
            'Client_country2': 'بلد الإقامة', 'Client_lang': 'اللغة الأم',
            'Client_edu': 'هل تخصصك تربية فنية',
            'Client_shade': 'هل يوجد لديك صعوبات في مشاهدة بعض الألوان (مثال : عمى الألوان)'
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Value is too long"),
                'Client_Year': ("Value is too long"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_AR
        self.fields['Client_edu'].choices = EDU_CHOICES_AR
        self.fields['Client_shade'].choices = EDU_CHOICES_AR

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='تاريخ الميلاد')


class Client_ColorForm_cz(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('Rok narození  :'), 'Client_sex': ('Pohlaví :'), 'Client_country1': ('Země, kde jste se narodil/a :'),
            'Client_country2': ('Země trvalého pobytu :'), 'Client_lang': ('Mateřský jazyk :'),
            'Client_edu': ('Umělecké vzdělání :'),
            'Client_shade': ('Máte potíže s vnímáním některých barev?')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Value is too long"),
                'Client_Year': ("Value is too long"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_CZ
        self.fields['Client_edu'].choices = EDU_CHOICES_CZ
        self.fields['Client_shade'].choices = EDU_CHOICES_CZ

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='Rok narození :')
