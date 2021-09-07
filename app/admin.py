from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import send,resume,contect,certificate,project

class showsend(ModelAdmin):
    list_display=["Email","Date"]
    search_fields=["Email","id"]
    list_filter=["Date","id"]

class showresume(ModelAdmin):
    list_display=["url"]

class showcontect(ModelAdmin):
    list_display=["Username","Email","Message"]
    search_fields=["Username","Email","id"]
    list_filter=["Date","id"]       

class showcertificate(ModelAdmin):
    list_display=["Topic","Image"]
    search_fields=["name"]
    list_filter=["id"]

class showproject(ModelAdmin):
    list_display=["Project_name","Image"]
    search_fields=["Project_name"]
    list_filter=["id"]    

admin.site.register(send,showsend)
admin.site.register(resume,showresume)
admin.site.register(contect,showcontect)
admin.site.register(certificate,showcertificate)
admin.site.register(project,showproject)