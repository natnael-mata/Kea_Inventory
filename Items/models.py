from django.db import models


STATUS_CHOICES = [ 
    ("A", "Active"), 
    ("I", "Inactive")
]

TRANS_TYPE_CHOICES = [
    ("SIN", "Stock IN"),
    ("SOU", "Stock Out"),
    ("REM", "Removed"),
    ("RET", "Returned"),
]

class Category(models.Model):
    category_id = models.CharField(max_length=5)
    category_name = models.CharField(max_length=100)
    parent_id = models.CharField(max_length=5)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    last_updated_on = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=100)

class Items(models.Model):
    item_id = models.CharField(max_length=10, primary_key=True)
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    #category_id 
    uom = models.CharField(max_length=3)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    last_updated_on = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=100)

class Items_Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    effective_date = models.DateField()
    #item_id (FK)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="A")
    remark = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    last_updated_on = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=100)


class Items_Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    #item_id (FK) = 
    price = models.DecimalField()
    effective_date = models.DateField()
    remark = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    last_updated_on = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=100)


class Trasactions(models.Model):
    trans_id = models.AutoField(primary_key=True)
    trans_type = models.CharField(max_length=3, choices=TRANS_TYPE_CHOICES)
    trans_date = models.DateTimeField(auto_now=True)
    #item_id (FK)
    amount = models.DecimalField()
    approved_on = models.DateTimeField(auto_now=True)
    approved_by = models.CharField(max_length=100)
    remark = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    last_updated_on = models.DateTimeField(auto_now=True)
    last_updated_by = models.CharField(max_length=100)
