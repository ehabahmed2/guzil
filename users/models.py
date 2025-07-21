from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Testimonial(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد المراجعة'),
        ('approved', 'معروض'),
        ('rejected', 'مرفوض'),
    ]
    
    customer_name = models.CharField(max_length=100, verbose_name="اسم العميلة")
    content = models.TextField(verbose_name="نص التعليق")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', 
                            verbose_name="الحالة")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "تقييم"
        verbose_name_plural = "التقييمات"
        ordering = ['-created_at']

    def __str__(self):
        return f"تعليق من {self.customer_name}"
    
    
    
    # admin user 
class AdminUser(AbstractUser):
    is_main_admin = models.BooleanField(default=False)
    class Meta:
        verbose_name = "مسؤول"
        verbose_name_plural = "المسؤولين"
