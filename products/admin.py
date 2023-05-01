from django.contrib import admin

from products import models

# Register your models here.

admin.site.register(models.Dish)
admin.site.register(models.Category)
admin.site.register(models.Payment)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.Menu)
admin.site.register(models.Basket)
