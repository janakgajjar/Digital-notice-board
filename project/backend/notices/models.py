from django.db import models
from django.utils import timezone


class Notice(models.Model):
    NOTICE_TYPE_CHOICES = [
        ('text', 'Text Notice'),
        ('image', 'Image Notice'),
        ('pdf', 'PDF Notice'),
    ]

    COLOR_CHOICES = [
        ('note-yellow', 'Yellow'),
        ('note-pink', 'Pink'),
        ('note-green', 'Green'),
        ('note-white', 'White'),
        ('note-lined', 'Lined White'),
    ]

    PIN_CHOICES = [
        ('pin-red', 'Red Pin'),
        ('pin-blue', 'Blue Pin'),
        ('pin-green', 'Green Pin'),
        ('pin-yellow', 'Yellow Pin'),
    ]

    title = models.CharField(max_length=200, verbose_name='શીર્ષક (Title)')
    description = models.TextField(blank=True, verbose_name='વર્ણન (Description)')
    notice_type = models.CharField(
        max_length=10,
        choices=NOTICE_TYPE_CHOICES,
        default='text',
        verbose_name='નોટિસ પ્રકાર (Notice Type)'
    )
    file = models.FileField(
        upload_to='uploads/',
        blank=True,
        null=True,
        verbose_name='ફાઇલ (Photo/PDF)',
        help_text='Photo (JPG, PNG) અથવા PDF upload કરો'
    )
    color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default='note-yellow',
        verbose_name='રંગ (Color)'
    )
    pin_color = models.CharField(
        max_length=20,
        choices=PIN_CHOICES,
        default='pin-red',
        verbose_name='પિન રંગ (Pin Color)'
    )
    expiry_date = models.DateField(verbose_name='સમાપ્તિ તારીખ (Expiry Date)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='બનાવ્યું (Created)')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='અપડેટ કર્યું (Updated)')
    is_active = models.BooleanField(default=True, verbose_name='સક્રિય છે? (Active)')
    department_choices = [ 
        ('BCA','BCA'),
        ('MCA','MCA'),
        ('PGDCA','PGDCA'),
    ]

    semester_choices= [
        ('sem-1','Semester 1'),
        ('sem-3','Semester 3'),
        ('sem-5','Semester 5'),
        ('all','All Semesters'), #pgdca or all semsesters
    ]

    is_common = models.BooleanField(
        default=False,
        help_text="Check this to make the notice appear on all department pages (બધા પેજ પર બતાવવા માટે આને ટિક કરો)"
    )

    department = models.CharField(max_length=10,choices=department_choices,default='BCA')
    semester = models.CharField(max_length=10,choices=semester_choices,default='sem-1')
    class Meta:
        verbose_name = 'નોટિસ (Notice)'
        verbose_name_plural = 'નોટિસ (Notices)'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def is_expired(self):
        return timezone.now().date() > self.expiry_date

    def get_file_extension(self):
        if self.file:
            return self.file.name.split('.')[-1].lower()
        return None

    def is_image(self):
        ext = self.get_file_extension()
        return ext in ['jpg', 'jpeg', 'png', 'gif', 'webp']

    def is_pdf(self):
        ext = self.get_file_extension()
        return ext == 'pdf'
