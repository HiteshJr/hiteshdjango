from django.db import models

# Create your models here.

class cart(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size  = models.IntegerField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=12)
    email = models.EmailField()

class users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    cart = models.CharField(max_length=100,default='[]')
    address  = models.CharField(max_length=500)
    orderhistory = models.CharField(max_length=1000,default='[]')


# Choices for categories
SHOE_CATEGORIES = [
    ('mens', "Men's Shoes"),
    ('womens', "Women's Shoes"),
    ('sports', "Sports Shoes"),
    ('formal', "Formal Shoes"),
    ('casual', "Casual Shoes"),
    ('sneakers', "Sneakers"),
    ('slippers', "Slippers"),
]

BRANDS = [
    ('nike', 'Nike'),
    ('adidas', 'Adidas'),
    ('puma', 'Puma'),
    ('reebok', 'Reebok'),
    ('bata', 'Bata'),
    ('woodland', 'Woodland'),
]

SIZES = [
    (5, 'Size 5'),
    (6, 'Size 6'),
    (7, 'Size 7'),
    (8, 'Size 8'),
    (9, 'Size 9'),
    (10, 'Size 10'),
    (11, 'Size 11'),
    (12, 'Size 12'),
]

class Shoe(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=20, choices=BRANDS)
    category = models.CharField(max_length=20, choices=SHOE_CATEGORIES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.FloatField(default=0.0)
    stock = models.PositiveIntegerField()
    # available_sizes = models.ManyToManyField('ShoeSize')
    rating = models.FloatField(default=0.0)
    # image = models.ImageField(upload_to='shoes/')
    image = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def discounted_price(self):
        return round(self.price * (1 - self.discount_percentage / 100), 2)

    def __str__(self):
        return f"{self.title} - {self.brand}"

class ShoeSize(models.Model):
    size = models.IntegerField(choices=SIZES)

    def __str__(self):
        return f"Size {self.size}"
