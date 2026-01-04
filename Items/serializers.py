from rest_framework import serializers
from django.db.models import Sum
from django.utils import timezone
from .models import Items, Category, Items_Status, STATUS_CHOICES, TRANS_TYPE_CHOICES, Items_Price, Transactions, Items_InitialAmount

# New Serializer for Item Name, Date, and Quantity
class ItemDateQtySerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item_id.item_name', read_only=True)
    
    class Meta:
        model = Items_InitialAmount
        fields = ['item_name', 'effective_date', 'quantity']


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
    category_name = serializers.CharField(source='category_id.category_name', read_only=True)
    available_balance = serializers.SerializerMethodField()
    latest_price = serializers.SerializerMethodField()

    class Meta:
        model = Items

        fields = [
            'item_id',
            'item_name',
            'category_id',  
            'category_name',
            'uom',
            'available_balance',
            'latest_price',
            'description',

        ]
        read_only_fields = fields 

    def get_available_balance(self, obj):
        request = self.context.get('request')
        report_date = timezone.now()
        if request and request.query_params.get('date'):
             report_date = request.query_params.get('date')

        # 1. Get latest Initial Amount before or on report_date
        initial_record = (
            Items_InitialAmount.objects
            .filter(item_id=obj.item_id, effective_date__lte=report_date)
            .order_by('-effective_date')
            .first()
        )

        initial_qty = initial_record.quantity if initial_record else 0
        start_date = initial_record.effective_date if initial_record else None

        # 2. Sum transactions
        trans_qs = Transactions.objects.filter(
            item_id=obj.item_id,
            trans_date__lte=report_date
        )

        if start_date:
            trans_qs = trans_qs.filter(trans_date__gt=start_date)

        total_trans_qty = trans_qs.aggregate(
            total=Sum('quantity')
        )['total'] or 0

        return initial_qty + total_trans_qty

    def get_latest_price(self, obj):
        request = self.context.get('request')
        report_date = timezone.now()
        if request and request.query_params.get('date'):
             report_date = request.query_params.get('date')
             
        latest_price_obj = (
            Items_Price.objects
            .filter(item_id=obj.item_id, effective_date__lte=report_date)
            .order_by('-effective_date')
            .first()
        )
        return latest_price_obj.unit_price if latest_price_obj else None

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
    is_latest = serializers.SerializerMethodField()

    class Meta:
        model = Items_Price
        fields = ['price_id',
                  'item_id',
                  'unit_price',
                  'currency',
                  'effective_date',
                  'remark',
                  'is_latest',
                  ]
        read_only_fields = ['created_on',
                            'last_updated_on',
                            'created_by',
                            'last_updated_by',  
                            ]
    
    def get_is_latest(self, obj):
        latest = Items_Price.objects.filter(item_id=obj.item_id).order_by('-effective_date').first()
        return latest and latest.price_id == obj.price_id

    @staticmethod
    def get_latest_price(item_id):
        """Helper to get the latest price object for an item."""
        return Items_Price.objects.filter(item_id=item_id).order_by('-effective_date').first()
        
          
class ItemsInitialAmountSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Items_InitialAmount
        fields = ['initial_amount_id',
                  'item_id',
                  'quantity',
                  'UOM',
                  'effective_date',
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
  
    def validate(self, attrs):
        trans_type = attrs.get('trans_type')
        quantity = attrs.get('quantity')
        item = attrs.get('item_id')
        trans_date = attrs.get('trans_date') or timezone.now()

        # 1. Validate quantity is positive
        if quantity is not None and quantity <= 0:
            raise serializers.ValidationError({
                "quantity": "Quantity must be greater than zero."
            })

        # 2. Check balance for stock-reducing transactions
        if trans_type in ['SOU', 'REM']:
            # Get latest initial amount <= trans_date
            initial_record = (
                Items_InitialAmount.objects
                .filter(item_id=item, effective_date__lte=trans_date)
                .order_by('-effective_date')
                .first()
            )

            if initial_record:
                initial_qty = initial_record.quantity
                start_date = initial_record.effective_date
            else:
                initial_qty = 0
                start_date = None

            # Sum transactions correctly
            trans_qs = Transactions.objects.filter(
                item_id=item,
                trans_date__lte=trans_date
            )

            # If initial exists, only sum AFTER effective_date
            if start_date:
                trans_qs = trans_qs.filter(trans_date__gt=start_date)

            total_trans_qty = trans_qs.aggregate(
                total=Sum('quantity')
            )['total'] or 0

            available_balance = initial_qty + total_trans_qty

            if available_balance < quantity:
                raise serializers.ValidationError({
                    "quantity": "Insufficient balance for this transaction."
                })
                
            # Negate quantity for storage
            attrs['quantity'] = -quantity

        return attrs
