from django.contrib import admin
from .models import *

# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ['*']

# class ImplementationAdmin(admin.ModelAdmin):
#     list_display = ['*']


admin.site.register(Project)
admin.site.register(Implementation)