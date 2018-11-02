from django.db import models
from django.contrib import admin

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField

    class Mate:
        ordering = ["name"]

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return ("itme_detail", None, {"object_id": self.id})

class Photo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="photos")
    caption = models.CharField(max_length=250, blank=True)

    class Mate:
        ordering = ["title"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ("photo_detail", None, {"object_id": self.id})

class PhotoInline(admin.StackedInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
