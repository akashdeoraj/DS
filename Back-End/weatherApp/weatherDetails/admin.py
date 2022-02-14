from django.contrib import admin

from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(coordinateWiseData)
class coordinateWiseDataAdmin(admin.ModelAdmin):
   list_display = ('id','longitude','latitude', 'gridId', 'gridx', 'gridy', 'today', 'tonight','monday','monday_night','tuesday','tuesday_night','wednesday','wednesday_night','thursday','thursday_night','friday','friday_night','saturday','saturday_night','sunday','sunday_night','lastupdated')