from django.db import models
import datetime

# Create your models here.

class Currency(models.Model):
    name=models.CharField(max_length=3)
    slug=models.SlugField(unique=False)



    class Meta:
            verbose_name = 'currency'
            verbose_name_plural = 'currencies'

    def __str__(self):
        return self.name




class CotData (models.Model):

    name=models.ForeignKey('Currency',on_delete=models.CASCADE)
    date=models.DateField()
    long=models.IntegerField()
    short=models.IntegerField()
    long_change=models.IntegerField()
    short_change=models.IntegerField()
    long_percent=models.FloatField()
    short_percent=models.FloatField()
    # slug=models.SlugField(unique=False)

    class Meta:
            verbose_name = 'cot data'
            verbose_name_plural = 'cot data'

    def net_positions(self):
        return self.long - self.short

    def str_date(self):
        return self.date.strftime('%m/%d/%Y')

    def __str__(self):
        return '{}    {}'.format(self.name,self.date)

