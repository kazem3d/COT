from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse, Http404
from .models import  CotData,Currency
from django.views.generic import ListView 
from django.contrib.auth.decorators import login_required

# Create your views here.

# class CotListView(ListView):
    # model = CotData
    # queryset=CotData.objects.filter(name__name='USD')

def CotListView(request):


    currency=CotData.objects.filter(name__name='USD')
    pairs=Currency.objects.all()
  

    context={
        'currency':currency,
        'pairs':pairs,
    }
    return render(request,'web/currency.html',context)


def currency_list(request,slug):
    slug=slug.upper()

    # currency=CotData.objects.filter(name__name=slug)
    pairs=Currency.objects.all()
    currency=get_list_or_404(CotData,name__name=slug)

    context={
        'currency':currency,
        'pairs':pairs,
    }
    return render(request,'web/currency.html',context)
    
@login_required
def import_data(request):
    import sqlite3

    conn=sqlite3.connect('report_database')
    curser=conn.cursor()

    #function for reading a table from date base and return data of row in list of list
    def read_from_datebase(table_name):
        _list=[]
        curser.execute('SELECT currency,date,long,short,long_change,short_change,long_change_percent,short_change_percent FROM %s ' %table_name)
        rows=curser.fetchall()
        for row in rows:
            row=list(row)
            _list.append(row)
        return _list

    database_list=read_from_datebase('main')
    for row in database_list:

        print("*****************")
        print(row)
        currency_name=Currency.objects.get(name=row[0])

        obj=CotData(name=currency_name,date=row[1],long=row[2],short=row[3],
                        long_change=row[4],short_change=row[5],long_percent=row[6],
                        short_percent=row[7])
        obj.save()

    return HttpResponse('import done')
