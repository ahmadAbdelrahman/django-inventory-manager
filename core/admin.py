from django.contrib import admin
from .models import Category, Product , Customer, SalesItem, SalesOrder

# Register your models here.

class SalesItemInline(admin.TabularInline):
    model = SalesItem
    extra = 1

class SalesOrderAdmin(admin.ModelAdmin):
    inlines = [SalesItemInline]


admin.site.register (Category)
admin.site.register (Product)
admin.site.register (Customer)
admin.site.register (SalesOrder, SalesOrderAdmin)

