from django.db import models

from users.models import User


# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=255)
    percent_obs = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_image')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.ForeignKey(to=Dish, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Basket for {self.user.username}"

    def sum(self):
        return self.products.price * self.quantity


class Payment(models.Model):
    status = models.BooleanField(default=False)
    type = models.CharField(max_length=12, default='Наличка')
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    dish = models.ForeignKey(to=Dish, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='order_items')


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.BooleanField(default=False)
    payment = models.OneToOneField(to=Payment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    place_number = models.PositiveIntegerField()


