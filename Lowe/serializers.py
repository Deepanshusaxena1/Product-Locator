from rest_framework import serializers
from . import models


class ShelfSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Shelf
        fields = ['ShelfLocationInFormat','Shelf_Id','Shelf_Block','Shelf_RowId','Shelf_Id_Location']


class ProductSerializers(serializers.ModelSerializer):
    Product_Location = ShelfSerializers(many=False, read_only=True)
    class Meta:
        model = models.Product
        fields = ['Product_Id', 'Product_Name', 'Product_category', 'Product_subcategory', 'Product_Price',
                  'Product_weight', 'Product_availability', 'Product_Location']
