from django.contrib import admin
from .models import Orden

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('usuario__username',)
    date_hierarchy = 'fecha_creacion'