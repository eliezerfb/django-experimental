from dal import autocomplete

from django.db.models.query_utils import Q
from django.http import HttpResponse

from greensale.core.models import Product


class ProductAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Product.objects.all()

        param_dict = {'name__icontains': self.q}

        if self.q:
            qs = qs.filter(Q(**param_dict))

        return qs


def get_price(request, pk):
    obj = Product.objects.get(pk=pk)
    return HttpResponse(obj.unit_price)


product_autocomplete = ProductAutocompleteView.as_view()
