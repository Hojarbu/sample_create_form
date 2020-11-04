from django.contrib import admin

# Register your models here.
from main.models import UserRequest, Category, Product

admin.site.register(UserRequest)
admin.site.register(Category)
admin.site.register(Product)
