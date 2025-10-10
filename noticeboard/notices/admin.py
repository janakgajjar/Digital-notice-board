from django.contrib import admin
from .models import notices
from django.utils import timezone #Import timezone

@admin.register(notices)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'expiry_date', 'is_expired'] #keep ' is_expired' here

    #define the custom method here

    def is_expired(self, obj):
        #Assuming you have an 'expiry_date field on your model
        if obj.expiry_date:
            return obj.expiry_date < timezone.now()
        return False # or whatever default you want
    
    is_expired.boolean = True # This will show a nice ✔️ or ❌ icon
    is_expired.short_description = 'Is Expired?' # Sets the column header text

    list_filter = ('expiry_date', 'author')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'

