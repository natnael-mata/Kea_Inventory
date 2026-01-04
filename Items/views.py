from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Items, Category, Items_Status, Items_Price, Items_InitialAmount, Transactions
from .serializers import ItemsSerializer, CategorySerializer, ItemsStatusSerializer, ItemReportSerializer, ItemsPriceSerializer, ItemsInitialAmountSerializer, TransactionsSerializer, ItemDateQtySerializer
from .stock_ledger import get_stock_ledger
class CategoryViewSet(viewsets.ModelViewSet):   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemsListViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemReportSerializer

class ItemsStatusViewSet(viewsets.ModelViewSet):
    queryset = Items_Status.objects.all()
    serializer_class = ItemsStatusSerializer

class ItemsPriceViewSet(viewsets.ModelViewSet):
    queryset = Items_Price.objects.all()
    serializer_class = ItemsPriceSerializer

class ItemsInitialAmountViewSet(viewsets.ModelViewSet):
    queryset = Items_InitialAmount.objects.all()
    serializer_class = ItemsInitialAmountSerializer

class TransactionsSerializerViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer

class ItemDateQtyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemDateQtySerializer

class StockLedgerView(APIView):
    def get(self, request, format=None):
        item_id = request.query_params.get('item_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        ledger_data = get_stock_ledger(item_id=item_id, start_date=start_date, end_date=end_date)
        return Response(ledger_data)