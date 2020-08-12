from django.db import models


# Create your models here.
class Shelf(models.Model):
    Shelf_Id = models.IntegerField()
    Shelf_Block = models.CharField(max_length=1)
    Shelf_RowId = models.IntegerField()
    Shelf_Id_Location = models.TextField()
    Shelf_Latitude = models.FloatField(null=False)
    Shelf_Longitude = models.FloatField(null=False)

    def ShelfLocationInFormat(self):
        return self.Shelf_Block + '-' + str(self.Shelf_RowId) + '-' + str(self.Shelf_Id)

    def __str__(self):
        return self.Shelf_Block + '-' + str(self.Shelf_RowId) + '-' + str(self.Shelf_Id)


class Product(models.Model):
    Product_Id = models.IntegerField(unique=True)
    Product_Name = models.CharField(max_length=50)
    Product_Category = models.CharField(max_length=50)
    Product_Sub_Category = models.CharField(max_length=50)
    Product_Price = models.CharField(max_length=50)
    Product_Weight = models.FloatField()
    Product_Location = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    Product_Availability = models.BooleanField(default=True)
    Product_On_Click_Count = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.Product_Id)
