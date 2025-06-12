from django import forms
from .models import Client_Color1
from .models import Client_Color2

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

SEX_CHOICES_RF = [
    ('', ''),
    ('мужской', 'мужской'),  # male, female, other
    ('женский', 'женский')
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

SEX_CHOICES_IND = [
    ('', ''),
    ('мужской', 'Pria'),  # male, female, other
    ('женский', 'Wanita'),
    ('другой', 'Lainnya')
]

EDU_CHOICES_IND = [
    ('', ''),
    ('да', 'Iya'),
    ('нет', 'Tidak'),
]

SEX_CHOICES_GR = [
    ('', ''),
    ('мужской', 'Άνδρας'),  # male, female, other
    ('женский', 'Γυναίκα'),
    ('другой', 'Άλλο')
]

EDU_CHOICES_GR = [
    ('', ''),
    ('да', 'ναι'),
    ('нет', 'όχι'),
]

EDU_CHOICES_FR = [
    ('', ''),
    ('да', 'oui'),
    ('нет', 'non'),
]

SEX_CHOICES_FR = [
    ('', ''),
    ('мужской', 'masculin'),  # male, female, other
    ('женский', 'féminin'),
    ('другой', 'autre')
]

EDU_CHOICES_CH = [
    ('', ''),
    ('да', '是'),
    ('нет', '否'),
]

SEX_CHOICES_CH = [
    ('', ''),
    ('мужской', '男'),  # male, female, other
    ('женский', '女'),
    ('другой', '其他')
]

EDU_CHOICES_KR = [
    ('', ''),
    ('да', '예'),
    ('нет', '아니오'),
]

SEX_CHOICES_KR = [
    ('', ''),
    ('мужской', '남성'),  # male, female, other
    ('женский', '여성'),
    ('другой', '기타 성별')
]

EDU_CHOICES_IC = [
    ('', ''),
    ('да', 'já'),
    ('нет', 'nei'),
]

SEX_CHOICES_IC = [
    ('', ''),
    ('мужской', 'karlkyns'),  # male, female, other
    ('женский', 'kvenkyns'),
    ('другой', 'annað')
]

EDU_CHOICES_SRB = [
    ('', ''),
    ('да', 'da'),
    ('нет', 'ne'),
]

SEX_CHOICES_SRB = [
    ('', ''),
    ('мужской', 'muški'),  # male, female, other
    ('женский', 'ženski'),
    ('другой', 'drugo')
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


class Client_ColorForm_reg(forms.ModelForm):
    class Meta:
        model = Client_Color2
        fields = (
            'Client_id', 'Client_Year', 'Client_sex',
            'Client_region', 'Client_edu', 'Client_shade')
        labels = {
            'Client_Year': ('Год Вашего рождения :'), 'Client_sex': ('Ваш пол :'),
            'Client_region': ('Субъект РФ :'),
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

        self.fields['Client_sex'].choices = SEX_CHOICES_RF
        self.fields['Client_edu'].choices = EDU_CHOICES_RU
        self.fields['Client_shade'].choices = EDU_CHOICES_RU

        self.fields['Client_region'].choices = REG_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940,
                                                        label='Год Вашего рождения :')


class Client_ColorForm_en(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('Year of birth :'), 'Client_sex': ('Gender :'), 'Client_country1': ('Country of birth :'),
            'Client_country2': ('Country of residence :'), 'Client_lang': ('Native language :'),
            'Client_edu': ('Have you studied art before?'),
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
            'Client_Year': ('Rok narození  :'), 'Client_sex': ('Pohlaví :'),
            'Client_country1': ('Země, kde jste se narodil/a :'),
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


class Client_ColorForm_ind(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('Tahun lahir  :'), 'Client_sex': ('Jenis kelamin :'),
            'Client_country1': ('Negara kelahiran :'),
            'Client_country2': ('Negara domisili :'), 'Client_lang': ('Bahasa asli :'),
            'Client_edu': ('Apakah Anda pernah belajar seni sebelumnya? :'),
            'Client_shade': (
                'Apakah Anda mengalami kesulitan dalam melihat warna-warna tertentu (misalnya, apakah Anda buta warna)?')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Value is too long"),
                'Client_Year': ("Value is too long"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_IND
        self.fields['Client_edu'].choices = EDU_CHOICES_IND
        self.fields['Client_shade'].choices = EDU_CHOICES_IND

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='Tahun lahir :')


class Client_ColorForm_gr(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('Έτος γέννησης  :'), 'Client_sex': ('Φύλο :'),
            'Client_country1': ('Χώρα γέννησης :'),
            'Client_country2': ('Χώρα κατοικίας :'), 'Client_lang': ('Μητρική γλώσσα :'),
            'Client_edu': ('Έχετε σπουδάσει τέχνες; :'),
            'Client_shade': (
                'Έχετε δυσκολία στο να βλέπετε συγκρεκριμένα χρώματα (π.χ., έχετε αχρωματοψία;)')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Value is too long"),
                'Client_Year': ("Value is too long"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_GR
        self.fields['Client_edu'].choices = EDU_CHOICES_GR
        self.fields['Client_shade'].choices = EDU_CHOICES_GR

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='Έτος γέννησης :')


class Client_ColorForm_fr(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('Année de naissance  :'), 'Client_sex': ('Genre :'),
            'Client_country1': ('Pays de naissance :'),
            'Client_country2': ('Pays de résidence :'), 'Client_lang': ('Langue maternelle :'),
            'Client_edu': ('Avez-vous étudié l’art ? :'),
            'Client_shade': (
                'Avez-vous des difficultés à distinguer certaines couleurs (i.e., êtes-vous daltonien)?')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Value is too long"),
                'Client_Year': ("Value is too long"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_FR
        self.fields['Client_edu'].choices = EDU_CHOICES_FR
        self.fields['Client_shade'].choices = EDU_CHOICES_FR

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='Année de naissance :')


class Client_ColorForm_ch(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('出生年份  :'), 'Client_sex': ('性別 :'),
            'Client_country1': ('出生國家 :'),
            'Client_country2': ('居住國家 :'), 'Client_lang': ('母語 :'),
            'Client_edu': ('您之前學過藝術嗎?'),
            'Client_shade': ('您是否有看到特定顏色的困難（您有辨色力異常，俗稱色盲嗎)?')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Value is too long"),
                'Client_Year': ("Value is too long"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_CH
        self.fields['Client_edu'].choices = EDU_CHOICES_CH
        self.fields['Client_shade'].choices = EDU_CHOICES_CH

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='出生年份 :')


class Client_ColorForm_kr(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('태어난해:'), 'Client_sex': ('성별:'),
            'Client_country1': ('태어난 국가:'),
            'Client_country2': ('거주 국가:'), 'Client_lang': ('모국어:'),
            'Client_edu': ('이전에 예술을 공부한 경험이 있습니까?'),
            'Client_shade': ('특정 색을 보는데 문제가 있습니까? (예시. 색맹)')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Value is too long"),
                'Client_Year': ("Value is too long"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_KR
        self.fields['Client_edu'].choices = EDU_CHOICES_KR
        self.fields['Client_shade'].choices = EDU_CHOICES_KR

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='태어난해:')


class Client_ColorForm_ic(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('Fæðingarár:'), 'Client_sex': ('Kyn:'),
            'Client_country1': ('Fæðingarland:'),
            'Client_country2': ('Búsetuland:'), 'Client_lang': ('Móðurmál:'),
            'Client_edu': ('Ertu menntað/ur/uð í listum?'),
            'Client_shade': ('Áttu í erfiðleikum með að sjá einhver litbrigði (svo sem vegna litblindu)?')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Value is too long"),
                'Client_Year': ("Value is too long"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_IC
        self.fields['Client_edu'].choices = EDU_CHOICES_IC
        self.fields['Client_shade'].choices = EDU_CHOICES_IC

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='Fæðingarár:')


class Client_ColorForm_srb(forms.ModelForm):
    class Meta:
        model = Client_Color1
        fields = (
            'Client_id', 'Client_Year', 'Client_sex', 'Client_country1', 'Client_country2', 'Client_lang', 'Client_edu',
            'Client_shade')
        labels = {
            'Client_Year': ('Godina rođenja:'), 'Client_sex': ('Pol:'),
            'Client_country1': ('Zemlja rođenja:'),
            'Client_country2': ('Zemlja u kojoj živite:'), 'Client_lang': ('Maternji jezik:'),
            'Client_edu': ('Da li ste studirali umetnost?'),
            'Client_shade': ('Da li imate problem sa razlikovanjem nekih boja? (na primer, da li imate neku formu daltonizma?)')
        }
        error_messages = {
            'Client_name': {
                'max_length': ("Value is too long"),
                'Client_Year': ("Value is too long"),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Client_sex'].choices = SEX_CHOICES_SRB
        self.fields['Client_edu'].choices = EDU_CHOICES_SRB
        self.fields['Client_shade'].choices = EDU_CHOICES_SRB

        self.fields['Client_country1'].choices = COU_CHOICES
        self.fields['Client_country2'].choices = COU_CHOICES

        self.fields['Client_Year'] = forms.IntegerField(max_value=2010, min_value=1940, label='Godina rođenja:')
