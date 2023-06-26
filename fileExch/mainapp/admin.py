from django.contrib import admin

# Register your models here.
from .models import User,Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "photo", "approver", "history"]



admin.site.register(User)
admin.site.register(Image,ImageAdmin)

