from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.urls import reverse


class DataModelUser(models.Model):
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=150)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class Subproduct(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='sub_products/%Y/%m/%d', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Субпродукт'
        verbose_name_plural = 'Субпродукты'


class Homework(models.Model):
    login = models.CharField(max_length=150)
    password = models.CharField(max_length=40)
    surname = models.CharField(max_length=80)
    phone = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    reg_date = models.DateField()
    check = models.CharField(max_length=10, blank=True, null=True)
    radio = models.CharField(max_length=10, blank=True, null=True)
    file = models.FileField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return 'Моя форма'

    class Meta:
        verbose_name = 'Экземпляр формы'
        verbose_name_plural = 'Заполненные формы'


class ExtendUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    phone = models.CharField(max_length=50, db_index=True, unique=True)
    message = models.BooleanField(default=True, verbose_name='Сообщение')

    class Meta(AbstractUser.Meta):
        pass
