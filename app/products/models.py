from django.db import models


class Category(models.Model):
    """
    Model to represent a product category

    Fields:
        name (CharField): name of the category
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Model to represent a product

    Fields:
        name (CharField): name of the product
        description (TextField): description of the product
        price (DecimalField): price of the product
        image_url (CharField): url of the product image
        stock_quantity (IntegerField): quantity of the product in stock
        category (ForeignKey): category of the product
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
