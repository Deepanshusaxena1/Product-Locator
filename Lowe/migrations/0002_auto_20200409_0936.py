# Generated by Django 3.0.4 on 2020-04-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lowe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_availability',
            new_name='Product_Availability',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_category',
            new_name='Product_Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_subcategory',
            new_name='Product_SubCategory',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_weight',
            new_name='Product_Weight',
        ),
        migrations.AddField(
            model_name='product',
            name='Product_OnClickCount',
            field=models.BigIntegerField(default=0),
        ),
    ]
