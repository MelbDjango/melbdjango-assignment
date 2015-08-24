from django.contrib import admin

# Register your models here.
from . import models

class GuestPostAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'name', 'email', 'comment', 'show')
    search_fields = ('name', 'email', 'comment')

admin.site.register(models.GuestPost, GuestPostAdmin)