from django.contrib import admin
from .models import CustomUser
from .models import Category, SubCategory,SubSubCategory, Product



admin.site.register(Category)
admin.site.register(SubSubCategory)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(CustomUser)

