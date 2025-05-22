from django.contrib import admin
from app.models import Client_Color1, Client_Color2
# Register your models here.

myModels = [Client_Color1, Client_Color2]
admin.site.register(myModels)
