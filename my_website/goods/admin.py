from django.contrib import admin

from goods.models import Categories, Products

# Register your models here.

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )} # автоматическое заполнение поле slug
    

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )} # автоматическое заполнение поле slug