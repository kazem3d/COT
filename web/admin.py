from django.contrib import admin
from .models import Currency,CotData

# Register your models here.
class CotDataAdmin(admin.ModelAdmin):
    list_display = ('name','date','long','short','long_change',
                    'short_change','long_percent','short_percent','net_positions')
    list_filter = ('name',)
    ordering = ['date']
    prepopulated_fields = {'slug': ('name',), }

admin.site.register(Currency)
admin.site.register(CotData,CotDataAdmin)

