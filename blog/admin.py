from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'status')
    list_filter = ('title', 'author', 'publish', 'status')
    search_fields = ('title', 'content')
    date_hierarchy = 'publish'

    # pesquisa
    prepopulated_fields = {'slug': ('title',)}
