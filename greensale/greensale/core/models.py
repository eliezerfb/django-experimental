from django.db import models


class Product(models.Model):
    name = models.CharField('nome', max_length=30)
    unit_price = models.DecimalField('preço unitário',
                                     max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Sale(models.Model):
    sale_date = models.DateField('data')
    number = models.IntegerField('número')

    def __str__(self):
        return self.number


class SaleItem(models.Model):
    sale = models.ForeignKey('Sale', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.DecimalField('quantidade', max_digits=6,
                                   decimal_places=2)
    unit_price = models.DecimalField('preço unitário',
                                     max_digits=6, decimal_places=2)
    total = models.DecimalField('total', max_digits=6, decimal_places=2)
