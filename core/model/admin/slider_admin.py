from django.contrib import admin

from core.model.slider import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'subtitle')
