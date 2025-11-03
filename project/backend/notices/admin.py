from django.contrib import admin
from django.utils.html import format_html
from .models import Notice



class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'department','semester','is_common','notice_type', 'expiry_date', 'is_active', 'created_at', 'file_preview', 'status_badge']
    list_filter = ['department','semester','is_common','notice_type', 'is_active', 'created_at', 'expiry_date']
    search_fields = ['title', 'description']
    date_hierarchy = 'created_at'
    list_editable = ['is_active']

    fieldsets = (
        ('મૂળભૂત માહિતી (Basic Information)', {
            'fields': ('title', 'description', 'notice_type')
        }),
        ('ફાઇલ અપલોડ (File Upload)', {
            'fields': ('department','semester','is_common'),
            'description': 'Photo (JPG, PNG) અથવા PDF upload કરો'
        }),
        ('દેખાવ (Appearance)', {
            'fields': ('color', 'pin_color')
        }),
        ('સમાપ્તિ અને સ્થિતિ (Expiry & Status)', {
            'fields': ('expiry_date', 'is_active')
        }),
    )

    def file_preview(self, obj):
        if obj.file:
            if obj.is_image():
                return format_html(
                    '<img src="{}" style="max-width: 100px; max-height: 100px; border-radius: 5px;" />',
                    obj.file.url
                )
            elif obj.is_pdf():
                return format_html(
                    '<a href="{}" target="_blank">📄 PDF જુઓ</a>',
                    obj.file.url
                )
        return '-'
    file_preview.short_description = 'પૂર્વાવલોકન (Preview)'

    def status_badge(self, obj):
        if obj.is_expired():
            return format_html(
                '<span style="background-color: #dc3545; color: white; padding: 3px 10px; border-radius: 3px;">સમાપ્ત (Expired)</span>'
            )
        else:
            return format_html(
                '<span style="background-color: #28a745; color: white; padding: 3px 10px; border-radius: 3px;">સક્રિય (Active)</span>'
            )
    status_badge.short_description = 'સ્થિતિ (Status)'

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }


admin.site.site_header = 'Gujarat Vidyapith - Admin Panel'
admin.site.site_title = 'Notice Board Admin'
admin.site.index_title = 'નોટિસ બોર્ડ વ્યવસ્થાપન (Notice Board Management)'
admin.site.register(Notice,NoticeAdmin)