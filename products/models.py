from django.db import models
from base.models import BaseModel
from  django.utils.text import slugify

# Create your models here.


class Category(BaseModel):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to='category')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save()

    def __str__(self) -> str:
        return str(self.category_name)


class Product(BaseModel):
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()
    product_description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save()

    def __str__(self) -> str:
        return str(self.product_name)


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to='product')
