
from django.db import models

# Create your models here.
class Product_record(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    manufacture_city = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

class Transaction_record (models.Model):
    transaction_id = models.IntegerField()
    transaction_amt = models.FloatField()
    transaction_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id
