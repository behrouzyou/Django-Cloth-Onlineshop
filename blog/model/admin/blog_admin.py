from django.contrib import admin

from blog.model.blog import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at', 'updated_at', 'created_at', 'visit_count')
    list_filter = ('is_published', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
