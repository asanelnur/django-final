from django.contrib import admin

from products import models

# Register your models here.

admin.site.register(models.Dish)
admin.site.register(models.Category)
admin.site.register(models.Restaurant)
admin.site.register(models.Menu)
admin.site.register(models.Basket)
