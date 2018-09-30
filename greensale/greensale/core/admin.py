from django.contrib import admin

from greensale.core.models import Product, Sale, SaleItem
from greensale.core.forms import SaleItemForm


class SaleItemModelAdmin(admin.TabularInline):
    model = SaleItem
    form = SaleItemForm
    extra = 1
    template = 'admin/core/tabular.html'


class SaleModelAdmin(admin.ModelAdmin):
    inlines = [SaleItemModelAdmin]


admin.site.register(Product)
admin.site.register(Sale, SaleModelAdmin)
