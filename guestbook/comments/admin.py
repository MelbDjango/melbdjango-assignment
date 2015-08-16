from django.contrib import admin

from .models import Comment, Message

class CommentAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
