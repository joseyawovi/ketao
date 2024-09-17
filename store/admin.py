from django.contrib import admin
from .models import CustomUser
from .models import Category, Subcategory, Product



admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product)
admin.site.register(CustomUser)

