from django.core.management.base import BaseCommand
from store.models import Category, SubCategory, SubSubCategory
from django.utils.text import slugify
import re

class Command(BaseCommand):
    help = 'Populate the database with initial data'

    def handle(self, *args, **kwargs):
        # Define categories, subcategories, and subsubcategories
        data = {
            "Clothing": {
                "Men's Clothing": ["Shirts", "Pants", "Jackets", "Suits", "Shorts"],
                "Women's Clothing": ["Dresses", "Tops", "Skirts", "Blouses", "Coats"],
                "Kids' Clothing": ["Boys", "Girls", "Infants", "T-Shirts", "Sweaters"],
            },
            "Electronics": {
                "Laptops": ["Gaming", "Business", "Ultrabooks", "Chromebooks", "2-in-1s"],
                "Mobile Phones": ["Smartphones", "Feature Phones", "Phablets", "Rugged Phones"],
                "Cameras": ["DSLR", "Mirrorless", "Point and Shoot", "Action Cameras", "Film Cameras"],
                "Accessories": ["Laptops Cases", "Chargers", "Headphones"],
            },
            "Shoes": {
                "Men's Shoes": ["Sneakers", "Formal", "Boots", "Loafers", "Sandals"],
                "Women's Shoes": ["Flats", "Heels", "Sneakers", "Ankle Boots", "Sandals"],
                "Kids' Shoes": ["Sneakers", "Sandals", "Dress Shoes", "Boots"],
            },
            "Watches": {
                "Men's Watches": ["Analog", "Digital", "Smart Watches", "Diving Watches"],
                "Women's Watches": ["Fashion", "Luxury", "Sports", "Bracelet Watches"],
            },
            "Jewellery": {
                "Necklaces": ["Gold", "Silver", "Fashion", "Pearl", "Diamond"],
                "Bracelets": ["Leather", "Beaded", "Metal", "Charm", "Friendship"],
                "Earrings": ["Studs", "Hoops", "Dangle", "Chandeliers"],
            },
            "Health and Beauty": {
                "Skincare": ["Moisturizers", "Cleansers", "Sunscreens", "Masks"],
                "Makeup": ["Face", "Eyes", "Lips", "Nail Polish"],
                "Haircare": ["Shampoos", "Conditioners", "Hair Treatments", "Styling Products"],
            },
            "Kids and Babies": {
                "Toys": ["Educational", "Outdoor", "Action Figures", "Dolls"],
                "Clothing": ["Baby", "Toddler", "Kids Accessories"],
                "Gear": ["Strollers", "Car Seats", "Baby Carriers"],
            },
            "Sports": {
                "Outdoor Sports": ["Hiking", "Camping", "Fishing", "Cycling"],
                "Indoor Sports": ["Gym Equipment", "Yoga", "Table Tennis", "Badminton"],
                "Team Sports": ["Football", "Basketball", "Baseball"],
            },
            "Home and Garden": {
                "Furniture": ["Living Room", "Bedroom", "Office", "Outdoor", "Storage"],
                "Garden": ["Plants", "Garden Tools", "Outdoor Furniture", "Decorations"],
                "Kitchen": ["Cookware", "Utensils", "Appliances", "Dining"],
            },
        }

        # Function to clean up the slug
        def create_slug(name, parent_slug=None):
            base_slug = slugify(re.sub(r"[^\w\s-]", "", name))
            if parent_slug:
                return slugify(f"{parent_slug}-{base_slug}")
            return base_slug

        # Add categories, subcategories, and subsubcategories to the database
        for category_name, subcategories in data.items():
            category_slug = create_slug(category_name)
            category, created = Category.objects.get_or_create(name=category_name, slug=category_slug)
            if created:
                self.stdout.write(f'Created category: {category_name}')
            else:
                self.stdout.write(f'Category already exists: {category_name}')

            for subcategory_name, subsubcategories in subcategories.items():
                subcategory_slug = create_slug(subcategory_name, parent_slug=category_slug)
                subcategory, created = SubCategory.objects.get_or_create(name=subcategory_name, category=category, slug=subcategory_slug)
                if created:
                    self.stdout.write(f'Created subcategory: {subcategory_name}')
                else:
                    self.stdout.write(f'Subcategory already exists: {subcategory_name}')

                for subsubcategory_name in subsubcategories:
                    subsubcategory_slug = create_slug(subsubcategory_name, parent_slug=subcategory_slug)
                    subsubcategory, created = SubSubCategory.objects.get_or_create(name=subsubcategory_name, subcategory=subcategory, slug=subsubcategory_slug)
                    if created:
                        self.stdout.write(f'Created subsubcategory: {subsubcategory_name}')
                    else:
                        self.stdout.write(f'Subsubcategory already exists: {subsubcategory_name}')
