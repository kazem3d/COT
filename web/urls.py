from django.contrib import admin
from django.urls import path
from .views import CotListView,currency_list,upload,HomePage

app_name='web'
urlpatterns = [

    path('',HomePage,name='home'),
    # path('',CotListView,name='home'),

    path('<slug:slug>/',currency_list,name='currency'),
    path('q/upload/',upload,name='upload'),


        ]