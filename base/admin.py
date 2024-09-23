from django.contrib import admin
from .models import User, Recipe, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Category)