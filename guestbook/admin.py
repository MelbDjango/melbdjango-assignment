from django.contrib import admin

from .models import GuestComment, SpamWord

# Register your models here.

admin.site.register(GuestComment)
admin.site.register(SpamWord)
