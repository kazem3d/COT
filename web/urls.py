from django.contrib import admin
from django.urls import path
from .views import CotListView,currency_list

app_name='web'
urlpatterns = [

    path('',CotListView.as_view(),name='home'),
    path('<slug:slug>/',currency_list,name='currency'),


        ]