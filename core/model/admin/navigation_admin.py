from django.contrib import admin

from core.model.navigation import Navigation


@admin.register(Navigation)
class NavigationAdmin(admin.ModelAdmin):
    list_display = ('title','link','is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)