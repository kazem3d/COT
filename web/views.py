from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import  CotData
from django.views.generic import ListView 

# Create your views here.

class CotListView(ListView):
    model = CotData

# class currency_list(ListView):
#     queryset=


def currency_list(request,slug):
    

    currency=CotData.objects.filter(slug=slug)
    # currency=get_object_or_404(CotData,slug=slug)

    context={
        'currency':currency,
    }
    return render(request,'web/currency.html',context)
