from django.contrib import admin

from .models import Record


#set the display boolean value from records.models to True if user 
#sselect it from dropdown menu from admin panel
def show_it(self, request, queryset):
    rows_updated = queryset.update(display=True)
    if rows_updated == 1:
        message_bit = "1 item was"
    else:
        message_bit = "%s items were" % rows_updated
    self.message_user(request, "%s successfully displayed at front-end." % message_bit)

#set the display boolean value from records.models to False if the user 
#selects it from dropdown menu from admin panel
def hide_it(self, request, queryset):
    rows_updated = queryset.update(display=False)
    if rows_updated == 1:
        message_bit = "1 item was"
    else:
        message_bit = "%s items were" % rows_updated
    self.message_user(request, "%s successfully hidden from front-end." % message_bit)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email_address', 'comment', 'entry_date', 'display')
    ordering = ('-entry_date',)
    search_fields= ('first_name', 'last_name', 'email_address')
    actions = (show_it, hide_it)


admin.site.register(Record, RecordAdmin)
