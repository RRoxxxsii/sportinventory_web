from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80)
    descript = models.TextField()
    photo =

class ProductCategory(models.Model):
    prod_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    descript = models.TextField()


class Product(models.Model):
    prod_name = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    prod_descript = models.TextField()
    prod_vendor = models.CharField()
    prod_amount = models.IntegerField(null=True)
    price = models.DecimalField()


