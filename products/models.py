from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
import uuid

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('skin-care', 'العناية بالبشرة'),
        ('hair-care', 'العناية بالشعر'),
        ('makeup', 'مكياج'),
        ('new', 'جديد'),
    ]
    
    
    name = models.CharField(max_length=255, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر", 
                              validators=[MinValueValidator(0)])
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="الفئة")
    stock = models.PositiveIntegerField(verbose_name="الكمية المتاحة")
    image = models.ImageField(upload_to='products/%y/%m/%d', verbose_name="صورة المنتج")
    is_best_seller = models.BooleanField(default=False, verbose_name="منتج مميز")
    is_available = models.BooleanField(default=True, verbose_name='هل المنتج متاح؟')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد المعالجة'),
        ('processing', 'جاري التجهيز'),
        ('shipped', 'تم الشحن'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغي'),
    ]
    order_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        verbose_name="رقم تتبع الطلب"
    )
    
    customer_name = models.CharField(max_length=100, verbose_name="اسم العميلة")
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    email = models.EmailField(blank=True, null=True, verbose_name="البريد الإلكتروني")
    address = models.TextField(verbose_name="العنوان")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ الإجمالي")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', 
                            verbose_name="حالة الطلب")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"
        ordering = ['-created_at']

    def __str__(self):
        return f"طلب {self.order_id} - {self.customer_name}"
    
    def save(self, *args, **kwargs):
        if not self.order_id:
            # First save to get an ID
            super().save(*args, **kwargs)
            # Now generate the order_id with the ID
            year = str(timezone.now().year)[-2:]
            random_part = uuid.uuid4().hex[:4].upper()
            self.order_id = f"GUZ-{year}{self.id:04d}-{random_part}"
            # Save again to store the order_id
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name="الطلب")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="المنتج")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    
    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"



