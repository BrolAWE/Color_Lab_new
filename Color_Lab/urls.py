from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('app.urls')), #color-lab.poll/
    path('admin/', admin.site.urls),
]
