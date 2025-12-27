from rest_framework import serializers
from .models import Items, Category, Items_Status
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 
                  'category_name', 
                  'description', 
                  'created_on', 
                  'created_by', 
                  'last_updated_on', 
                  'last_updated_by']
        
class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['item_id', 
                  'item_name', 
                  'description', 'category_id', 'uom', 'created_on', 'created_by', 'last_updated_on', 'last_updated_by']
        depth = 1  # To include related Category details
class ItemsStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items_Status
        fields = ['status_id', 'effective_date', 'item_id', 'status', 'remark', 'created_on', 'created_by', 'last_updated_on', 'last_updated_by']
        depth = 1  # To include related Items details       