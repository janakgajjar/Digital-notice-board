from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class notices(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to='myapp/',blank=True,null=True)
    attachment = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="Attachment")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_notices')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created_date")
    expiry_date = models.DateField(verbose_name="Expiry_date")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_notices')
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.expiry_date < timezone.now():
            self.is_active = False
        super().save(*args, ** kwargs)

    def __str__(self):
        return self.title