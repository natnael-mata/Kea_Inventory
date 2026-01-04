from django.test import TestCase
from django.utils import timezone
from .models import Items, Category, Items_InitialAmount, Transactions

class ItemBalanceTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            category_id="CAT1",
            category_name="Test Category",
            description="Test Description",
            created_by="TestUser"
        )
        self.item = Items.objects.create(
            item_id="ITEM1",
            item_name="Test Item",
            description="Test Item Description",
            category_id=self.category,
            uom="PCS",
            created_by="TestUser"
        )

    def test_item_current_balance(self):
        # 1. Set Initial Amount: 100
        Items_InitialAmount.objects.create(
            item_id=self.item,
            quantity=100,
            effective_date=timezone.now().date(),
            UOM="PCS",
            created_by="TestUser"
        )

        # 2. Add Transactions
        # Stock In: +50
        Transactions.objects.create(
            trans_type='SIN',
            item_id=self.item,
            quantity=50,
            created_by="TestUser"
        )
        # Stock Out: -20 (Stored as negative in correct implementation, but let's assume raw positive input handling if serializer does it, 
        # BUT Transactions model stores raw quantity usually? 
        # Wait, the serializer previously seen negates it. Let's create it as the system would store it.
        # If I use the model directly, I need to be careful. 
        # Current TransactionsSerializer logic negates it. 
        # So I will store -20 directly to simulate a saved record.
        Transactions.objects.create(
            trans_type='SOU',
            item_id=self.item,
            quantity=-20, 
            created_by="TestUser"
        )

        # Expected Balance: 100 + 50 - 20 = 130

        # Check via Serializer (Need to import locally to avoid early import issues if file is broken)
        from .serializers import ItemDateQtySerializer
        
        # The serializer expects an Item instance now (per our plan)
        serializer = ItemDateQtySerializer(self.item)
        data = serializer.data
        
        print(f"DEBUG: Calculated Quantity: {data.get('quantity')}")

        self.assertEqual(data.get('item_name'), "Test Item")
        # We expect a quantity field
        self.assertEqual(data.get('quantity'), 130)
