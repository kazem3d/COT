from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import  CotData,Currency
from django.views.generic import ListView 

# Create your views here.

class CotListView(ListView):
    model = CotData


def currency_list(request,slug):
    slug=slug.upper()

    currency=CotData.objects.filter(name__name=slug)
    pairs=Currency.objects.all()
    # currency=get_object_or_404(CotData,slug=slug)

    context={
        'currency':currency,
        'pairs':pairs,
    }
    return render(request,'web/currency.html',context)
