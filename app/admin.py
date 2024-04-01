from django.contrib import admin
from . models import Cat,Post,register,total_views

class CAT(admin.ModelAdmin):
    list_display = ("id","name")

class POST(admin.ModelAdmin):
    list_display = ("id","image1","image2","pdis1","ptitle","pcat","pdis2")
    search_fields = ("id","image1","image2","pdis1","ptitle","pcat","pdis2")
    list_filter = ('pcat',)
class REG(admin.ModelAdmin):
    list_display = ("id","email","password")

class TOTAL(admin.ModelAdmin):
    list_display = ("id","uid","pid")
admin.site.register(total_views,TOTAL)
admin.site.register(register,REG)
admin.site.register(Post,POST)
admin.site.register(Cat,CAT)

# Register your models here.
