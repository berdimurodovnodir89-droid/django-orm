from django.db import models


class Product(models.Model):

    class CurrencyChoices(models.TextChoices):
        UZS = 'uzs', 'UZS'
        USD = 'usd', 'USD'

    class StatusChoices(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        ACTIVE = 'active', 'Active'
        ARCHIVED = 'archived', 'Archived'

    name = models.CharField(max_length=255)
    slug = models.SlugField(null=False, blank=False)
    description = models.TextField(null=False, blank=True, default='')
    short_description = models.CharField(max_length=1024, null=False, blank=True, default='')
    sku = models.CharField(max_length=32)
    barcode = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CurrencyChoices.choices, default=CurrencyChoices.USD)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.FloatField()

    stock_quantity = models.PositiveIntegerField()
    min_stock_level = models.PositiveIntegerField()
    max_stock_level = models.PositiveIntegerField()
    is_in_stock = models.BooleanField(default=True)
    warehouse_location = models.CharField(max_length=255)
    reserved_quantity = models.PositiveIntegerField()

    thumbnail = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    status = models.CharField(max_length=32, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "products"
        ordering = ["-updated_at"]
        verbose_name = "Product"
        verbose_name_plural = 'Products'
        

    def __str__(self):
        return f"{self.id}. {self.name}"
        