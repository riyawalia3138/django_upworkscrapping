from django.contrib import admin
from .models import upwork, dataa, my_table


# Register your models here.

@admin.register(upwork, dataa, my_table)
class DefaultAdmin(admin.ModelAdmin):
    pass
