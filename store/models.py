from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)  # Add phone field

    def __str__(self):
        return self.username  # Or customize the return value as needed



class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to now when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated to now on save
    hot = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to now when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated to now on save

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubSubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to now when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated to now on save

    subcategory = models.ForeignKey(SubCategory, related_name='subsubcategories', on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(SubSubCategory, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subsubcategory = models.ForeignKey(SubSubCategory, null=True, blank=True, on_delete=models.SET_NULL, related_name='products')
    principal_image = models.ImageField(upload_to='product_images/principal/')
    hover_image = models.ImageField(upload_to='product_images/hover/', blank=True, null=True)
    additional_image_1 = models.ImageField(upload_to='product_images/additional/', blank=True, null=True)
    additional_image_2 = models.ImageField(upload_to='product_images/additional/', blank=True, null=True)
    additional_image_3 = models.ImageField(upload_to='product_images/additional/', blank=True, null=True)
    additional_image_4 = models.ImageField(upload_to='product_images/additional/', blank=True, null=True)
    hot = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)
    stock = models.IntegerField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to now when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated to now on save

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
