
from dal import autocomplete

from django import forms

from greensale.core.models import Product, SaleItem


class SaleItemForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=autocomplete.ModelSelect2(url='core:product-autocomplete')
    )

    class Meta:
        model = SaleItem
        fields = ('product', 'quantity', 'unit_price', 'total')
