from django.urls import path

from greensale.core.views import product_autocomplete, get_price

app_name = 'core'

urlpatterns = [
    path('product-autocomplete/', product_autocomplete,
         name='product-autocomplete'),
    path('get-price/<int:pk>', get_price, name='get-price')
]
