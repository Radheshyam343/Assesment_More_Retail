from rest_framework import serializers
from .models import Product_record,Transaction_record

# class Product_recordSerializer(serializers.Serializer):
#     product_id = serializers.IntegerField()
#     product_name = serializers.CharField(max_length=100)
#     manufacture_city = serializers.CharField(max_length=100)


        
# class Transaction_recordSerializer (serializers.Serializer):
#     transaction_id = serializers.IntegerField()
#     product_id = serializers.IntegerField()
#     transaction_amt = serializers.FloatField()
#     transaction_datetime = serializers.DateTimeField(auto_add_now=True)


class Product_recordSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product_record
        fields= '__all__'

class Transaction_recordSerializer (serializers.ModelSerializer):
    class Meta:
        model= Transaction_record
        fields = '__all__'
