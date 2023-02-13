from django.contrib import admin

from instagram.models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['message']
    list_display = ['pk', 'message', 'author']