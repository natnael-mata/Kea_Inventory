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
    last_updated_on = models.DateTimeField(auto_now=True, 
                                           blank= True, 
                                           null= True)
    last_updated_by = models.CharField(max_length=100,
                                       blank= True, 
                                       null= True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        db_table = 'Category'

class Items(models.Model):
    item_id = models.CharField(max_length=10, primary_key=True)
    item_name = models.CharField(max_length=100)
    description = models.TextField(blank = True, null = True)
    category_id = models.ForeignKey (Category, 
                                     on_delete = models.CASCADE,
                                     related_name = 'items',
                                     db_column = 'category_id') 
    uom = models.CharField(max_length=3)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    last_updated_on = models.DateTimeField(auto_now=True, 
                                           blank= True, 
                                           null= True)
    last_updated_by = models.CharField(max_length=100,
                                       blank= True, 
                                       null= True)

    def __str__(self):
        return self.item_name
    
    class Meta:
        db_table = 'Items'

class Items_Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    effective_date = models.DateField()
    item_id =  models.ForeignKey(Items, 
                                 on_delete=models.CASCADE,
                                 db_column = 'item_id',
                                 related_name= 'status')
    status = models.CharField(max_length=1, 
                              choices=STATUS_CHOICES, 
                              default="A")
    remark = models.TextField(blank=True, null= True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    last_updated_on = models.DateTimeField(auto_now=True, 
                                           blank= True, 
                                           null= True)
    last_updated_by = models.CharField(max_length=100,
                                       blank= True, 
                                       null= True)

    class Meta:
        db_table = 'Items_Status'

class Items_Price(models.Model):
    price_id = models.AutoField(primary_key=True)
    item_id =  models.ForeignKey(Items, 
                                 on_delete=models.CASCADE,
                                 db_column = 'item_id',
                                 related_name= 'price')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField()
    remark = models.TextField(blank= True, null= True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    last_updated_on = models.DateTimeField(auto_now=True, 
                                           blank= True, 
                                           null= True)
    last_updated_by = models.CharField(max_length=100,
                                       blank= True, 
                                       null= True)

    class Meta:
         db_table = 'Items_Price'
    
class Transactions(models.Model):
    trans_id = models.AutoField(primary_key=True)
    trans_type = models.CharField(max_length=3, choices=TRANS_TYPE_CHOICES)
    trans_date = models.DateTimeField(auto_now=True)
    item_id =  models.ForeignKey(Items, 
                                 on_delete=models.CASCADE,
                                 db_column = 'item_id',
                                 related_name= 'trans')
    amount = models.IntegerField()
    approved_on = models.DateTimeField(auto_now=True,
                                       blank= True, 
                                       null= True)
    approved_by = models.CharField(max_length=100,
                                   blank= True, 
                                   null= True)
    remark = models.TextField(blank= True, null= True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    last_updated_on = models.DateTimeField(auto_now=True, 
                                           blank= True, 
                                           null= True)
    last_updated_by = models.CharField(max_length=100,
                                       blank= True, 
                                       null= True)
    
    class Meta:
         db_table = 'Transactions'