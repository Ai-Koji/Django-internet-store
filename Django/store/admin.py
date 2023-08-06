from django.contrib import admin
from .models import *

class catalogAdmin(admin.ModelAdmin):
    filter_horizontal = ('subdirectories',)

class productAdmin(admin.ModelAdmin):
    filter_horizontal = ('subdirectories','images', 'additional_images',)


admin.site.register(Catalog, catalogAdmin)
admin.site.register(Product, productAdmin)
admin.site.register(Service)
admin.site.register(Subdirectory)