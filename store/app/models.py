from django.db import models

from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Product title')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")
    description = models.TextField(
        blank=True, verbose_name='Product description')
    photo = models.ImageField(
        upload_to="product_photos/%Y/%m/%d", verbose_name='Product photo')
    cost = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Product create time')
    time_update = models.DateTimeField(
        auto_now=True, verbose_name='Product update time')
    is_published = models.BooleanField(default=True)
    categ = models.ForeignKey(
        'Category', on_delete=models.PROTECT,  verbose_name='Product category',
        related_name='get_products')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['title']


class Category(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class Customer(models.Model):

    first_name = models.CharField(max_length=50, verbose_name='Name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')

    user_email = models.EmailField(max_length=70, blank=True, unique=True)
    password = models.CharField(max_length=50)

    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Product create time')
    time_update = models.DateTimeField(
        auto_now=True, verbose_name='Product update time')

    def __str__(self):
        return self.user_email

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['id']
