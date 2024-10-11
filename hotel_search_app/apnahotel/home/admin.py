from django.contrib import admin
from .models import *
# Register your models here.
class Hoteladmin(admin.ModelAdmin):
    list_display=['hotel_name','hotel_price','hotel_description']



    
admin.site.register(Amenities)
admin.site.register(Hotel ,Hoteladmin)
admin.site.register(HotelImage)