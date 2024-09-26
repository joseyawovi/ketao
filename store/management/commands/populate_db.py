from django.core.management.base import BaseCommand
from store.models import Category, SubCategory, SubSubCategory
from django.utils.text import slugify

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

        # Add categories, subcategories, and subsubcategories to the database
        for category_name, subcategories in data.items():
            category, created = Category.objects.get_or_create(name=category_name, slug=slugify(category_name))
            if created:
                self.stdout.write(f'Created category: {category_name}')
            else:
                self.stdout.write(f'Category already exists: {category_name}')

            for subcategory_name, subsubcategories in subcategories.items():
                subcategory, created = SubCategory.objects.get_or_create(name=subcategory_name, category=category, slug=slugify(subcategory_name))
                if created:
                    self.stdout.write(f'Created subcategory: {subcategory_name}')
                else:
                    self.stdout.write(f'Subcategory already exists: {subcategory_name}')

                for subsubcategory_name in subsubcategories:
                    subsubcategory, created = SubSubCategory.objects.get_or_create(name=subsubcategory_name, subcategory=subcategory, slug=slugify(subsubcategory_name))
                    if created:
                        self.stdout.write(f'Created subsubcategory: {subsubcategory_name}')
                    else:
                        self.stdout.write(f'Subsubcategory already exists: {subsubcategory_name}')
