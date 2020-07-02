from django.shortcuts import render,get_list_or_404,redirect
from django.http import HttpResponse, Http404
from .models import  CotData,Currency
from django.views.generic import ListView 
from django.contrib.auth.decorators import login_required
import sqlite3
from django.core.files.storage import FileSystemStorage


# Create your views here.

# class CotListView(ListView):
    # model = CotData
    # queryset=CotData.objects.filter(name__name='USD')

def CotListView(request):

    currency=CotData.objects.filter(name__name='USD').order_by('-date')[:15]
    pairs=Currency.objects.all()

    labels = []
    data = []
    long_change=[]
    short_change=[]
    for i in currency:
        labels.append(i.str_date())
        data.append(i.net_positions())
        long_change.append(i.long_change)
        short_change.append(i.short_change)


    labels=labels[::-1]
    data=data[::-1]
    long_change=long_change[::-1]
    short_change=short_change[::-1]
    
    context={
        'currency':currency,
        'pairs':pairs,
        'labels': labels,
        'data': data,
        'long_change':long_change,
        'short_change':short_change,
        'currency_name' : [' Net position of : USD'],
  

    }
    return render(request,'web/currency.html',context)


def currency_list(request,slug):
    slug=slug.upper()

    # currency=CotData.objects.filter(name__name=slug)
    pairs=Currency.objects.all()
    currency=get_list_or_404(CotData.objects.order_by('-date'),name__name=slug)[:15]

    labels = []
    data = []
    long_change=[]
    short_change=[]
        
    for i in currency:
        labels.append(i.str_date())
        data.append(i.net_positions())
        long_change.append(i.long_change)
        short_change.append(i.short_change)

    labels=labels[::-1]
    data=data[::-1]
    long_change=long_change[::-1]
    short_change=short_change[::-1]

    context={
        'currency':currency,
        'pairs':pairs,
        'labels': labels,
        'data': data,
        'long_change':long_change,
        'short_change':short_change,
        'currency_name' :[slug]
    }
    return render(request,'web/currency.html',context)
    
@login_required
def upload(request):

    #function for reading a table from date base and return data of row in list of list
    def read_from_datebase(table_name):
        _list=[]
        curser.execute('SELECT currency,date,long,short,long_change,short_change,long_change_percent,short_change_percent FROM %s ' %table_name)
        rows=curser.fetchall()
        for row in rows:
            row=list(row)
            _list.append(row)
        return _list

    if request.method == "POST":

        upload_file=request.FILES['myfile']
        fs = FileSystemStorage()
        fs.delete('report_database')
        filename = fs.save('report_database', upload_file)
       
        conn=sqlite3.connect('media/report_database')
        curser=conn.cursor()

        input_date=request.POST.get('date')

        database_list=read_from_datebase('main')
        for row in database_list:

            date=row[1]
            if date == input_date :
                print("*****************")
                print(row)
                currency_name=Currency.objects.get(name=row[0])

                obj=CotData(name=currency_name,date=date,long=row[2],short=row[3],
                                long_change=row[4],short_change=row[5],long_percent=row[6],
                                short_percent=row[7])
                obj.save()
        return HttpResponse('uploading done')
        

    return render (request,'web/upload.html')