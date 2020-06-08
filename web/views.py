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

    row1=read_from_datebase('main')[1]

    print("*****************")
    print(row1)
    # obj=CotData(name=row1[0],date=row1[1],long=row1[2])
    # obj.save()

    return HttpResponse('import done')
