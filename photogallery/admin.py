from django.contrib import admin
from photogallery.models import Item, ItemAdmin, Photo

# Register your models here.
admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
