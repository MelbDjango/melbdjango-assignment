from django.contrib import admin
from .models import Post

def hide_post(modeladmin, request, queryset):
	queryset.update(status='h')
hide_post.short_description = "Hide this post"


class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'text']
    ordering = ['time']
    actions = [hide_post]

admin.site.register(Post, PostAdmin)

# Register your models here.
