from django import forms
from .models import notices

class NoticeForm(forms.ModelForm):

    class Meta:
        model = notices
        fields = ['title', 'description', 'image', 'expiry_date']
        widgets = { 'expiry_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'text': forms.Textarea(attrs={'rows': 4}),
            }