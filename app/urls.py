"""
Адресация приложения,
для каждой страницы - свой адрес
"""
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('page1/', views.indexLn, name='indexLn'),
    path('page2/', views.index1, name='index1'),
    path('page3/', views.index2, name='index2'),
    path('page4/', views.index3, name='index3'),
    path('page5/', views.index4, name='index4'),
    path('page6/', views.index5, name='index5'),
    path('page7/', views.index6, name='index6'),
    path('page8/', views.index7, name='index7'),
    path('page9/', views.index8, name='index8'),
    path('page10/', views.index9, name='index9'),
    path('page11/', views.index10, name='index10'),
    path('page12/', views.index11, name='index11'),
    path('page13/', views.index12, name='index12'),
    path('page14/', views.index13, name='index13'),
    path('page15/', views.index14, name='index14'),
    path('page_end/', views.index15, name='index15'),
    path('indexend/', views.indexend, name='indexend'),
    path('export_xls/', views.export_xls, name='export_xls'),
]
