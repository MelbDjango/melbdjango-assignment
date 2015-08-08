from django.contrib import admin

from . import models

class EntryAdmin(admin.ModelAdmin):
    list_display = ('date', 'fname', 'lname', 'email', 'visible', 'comment')
    list_filter = ('date', 'fname', 'lname', 'visible')
    search_fields = ('fname', 'lname', 'comment')

admin.site.register(models.Entry, EntryAdmin)
