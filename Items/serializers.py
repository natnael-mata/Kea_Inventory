from rest_framework import serializers
from .models import Items, Category, Items_Status, STATUS_CHOICES, TRANS_TYPE_CHOICES, Items_Price, Transactions, Items_InitialAmount

#Categry Serializers to handle both read and write operations
class CategorySerializer(serializers.ModelSerializer):
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
        extra_kwargs = {
            'category_id': {'required': True},
            'category_name': {'required': True},
        }

#Items Serializers for read and write operations        
class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['item_id', 
                  'item_name', 
                  'description', 
                  'category_id', 
                  'uom', 
                  ]
        read_only_fields = ['created_on',
                            'last_updated_on',
                            'created_by',
                            'last_updated_by',
                            ]
        extra_kwargs = {
                'item_id': {'required': True},
                'item_name': {'required': True},
                'category_id': {'required': True},
        }
#Items Report Serializer for detailed read operations
class ItemReportSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='Category.category_name', read_only=True)
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

class ItemsStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items_Status
        fields = ['status_id', 
                  'effective_date', 
                  'item_id', 
                  'status', 
                  'remark', 
                  'created_on', 
        ]
        read_only_fields = ['created_on',
                            'last_updated_on',
                            'created_by',
                            'last_updated_by',  
                            ]

class ItemsPriceSerializer(serializers.ModelSerializer):        
    class Meta:
        model = Items_Price
        fields = ['price_id',
                  'item_id',
                  'unit_price',
                  'currency',
                  'effective_date',
                  'remark',
                  ]
        read_only_fields = ['created_on',
                            'last_updated_on',
                            'created_by',
                            'last_updated_by',  
                            ]
class TransactionsSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Transactions
        fields = ['trans_id',
                  'trans_type',
                  'trans_date', 
                    'item_id',
                    'quantity',
                    'approved_on',
                    'approved_by',
                    'remark',
                        ]
        read_only_fields = ['created_on',
                            'last_updated_on',
                            'created_by',
                            'last_updated_by',  
                            ]
        def validate_trans(self, data)
            trans_type = data.get('trans_type')
            amount = data.get('amount')
            if trans_type == 'OUT' and amount > available_stock:
                raise serializers.ValidationError("Insufficient stock for OUT transaction.")
            return data
            
class ItemsInitialAmountSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Items_InitialAmount
        fields = ['initial_amount_id',
                  'item_id',
                  'quantity',
                    'UOM',
                  'effective_date',
                  'remark',
                        ]
        read_only_fields = ['created_on',
                            'last_updated_on',
                            'created_by',
                            'last_updated_by',  
                            ]
