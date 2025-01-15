from django.contrib import admin
from .models import Profile

# Profile admin panel
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # ستون‌های نمایشی در لیست
    list_display = ['author', 'display_image']
    
    # فیلدهای جستجو
    search_fields = ['author']
    
    # نمایش تصویر در ادمین
    def display_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100" />'
        return 'بدون تصویر'
    
    display_image.short_description = 'تصویر'
    display_image.allow_tags = True