from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ItemInfo(models.Model):
    class Meta:
        db_table="iteminfo"
    item_url = models.CharField(max_length=50)
    item_image1 = models.ImageField(blank=True, upload_to = 'images/')
    item_image2 = models.ImageField(blank=True)
    item_image3 = models.ImageField(blank=True)
    item_image4 = models.ImageField(blank=True)
    item_image5 = models.ImageField(blank=True)
    item_image6 = models.ImageField(blank=True)
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    Item_desc = models.TextField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
