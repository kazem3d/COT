from django.contrib import admin
from django.urls import path
from .views import CotListView,currency_list,import_data,upload

app_name='web'
urlpatterns = [

    path('',CotListView,name='home'),
    path('<slug:slug>/',currency_list,name='currency'),
    path('q/import/',import_data,name='import_data'),
    path('q/upload/',upload,name='upload'),


        ]