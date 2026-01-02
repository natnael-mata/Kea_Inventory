from rest_framework import serializers
from .models import Items, Category, Items_Status, STATUS_CHOICES, TRANS_TYPE_CHOICES, Items_Price, Transactions

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 
                  'category_name',
                  'parent_id', 
                  'description']
        read_only_fields = ['created_on',
                            'last_updated_on',
                            'created_by',
                            'last_updated_by',
]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 
                  'category_name',
                  'parent_id', 
                  'description', 
                  'created_on', 
                  'created_by', 
                  'last_updated_on', 
                  'last_updated_by']
        read_only_fields = fields

class ItemReportSerializer(serializers.ModelSerializer):
    
    category_name = serializers.CharField(source='category_id.category_name', read_only=True)
    
    class Meta:
        model = Items

        fields = [
            'item_id',
            'item_name',
            'category_id',  
            'category_name',
            'uom',
            'description',
        ]
        read_only_fields = fields 
        
class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['item_id', 
                  'item_name', 
                  'description', 
                  'category_id', 
                  'uom', 
                  'created_on', 
                  'created_by', 
                  'last_updated_on', 
                  'last_updated_by']
        depth = 1  # To include related Category details
class ItemsStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items_Status
        fields = ['status_id', 
                  'effective_date', 
                  'item_id', 
                  'status', 
                  'remark', 
                  'created_on', 
                  'created_by', 
                  'last_updated_on', 
                  'last_updated_by']
        depth = 1  # To include related Items details       

        read_only_fields = ['created_on',
                            'last_updated_on',
                            'created_by',
                            'last_updated_by',  
                            ]
class ItemsStatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items_Status
        fields = ['status_id', 
                  'effective_date', 
                  'item_id', 
                  'status', 
                  'remark']
        depth = 1  # To include related Items details
        read_only_fields = ['created_on',
                            'last_updated_on',
                            'created_by',
                            'last_updated_by',  
                            ]
class ItemsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['item_id', 
                  'item_name', 
                  'description', 
                  'category_id', 
                  'uom']
        depth = 1  # To include related Category details
        read_only_fields = ['created_on',
                            'last_updated_on',
                            'created_by',
                            'last_updated_by',
]
        
