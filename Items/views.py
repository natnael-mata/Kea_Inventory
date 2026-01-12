from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Items, Category, Items_Status, Items_Price, Items_InitialAmount, Transactions
from .serializers import ItemsSerializer, CategorySerializer, ItemsStatusSerializer, ItemReportSerializer, ItemsPriceSerializer, ItemsInitialAmountSerializer, TransactionsSerializer, ItemDateQtySerializer
from .stock_ledger import get_stock_ledger
from drf_spectacular.utils import extend_schema
from Users.permissions import IsAdminOrStoreKeeper, IsAdminOrSupervisorOrStoreKeeper, IsAdminUser

class CategoryViewSet(viewsets.ModelViewSet):   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
   # permission_classes = [IsAdminOrSupervisorOrStoreKeeper]

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
   # permission_classes = [IsAdminOrSupervisorOrStoreKeeper]

class ItemsListViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemReportSerializer
  #  permission_classes = [IsAdminOrSupervisorOrStoreKeeper]

class ItemsStatusViewSet(viewsets.ModelViewSet):
    queryset = Items_Status.objects.all()
    serializer_class = ItemsStatusSerializer
   # permission_classes = [IsAdminOrSupervisorOrStoreKeeper]

class ItemsPriceViewSet(viewsets.ModelViewSet):
    queryset = Items_Price.objects.all()
    serializer_class = ItemsPriceSerializer
   # permission_classes = [IsAdminOrSupervisorOrStoreKeeper]

class ItemsInitialAmountViewSet(viewsets.ModelViewSet):
    queryset = Items_InitialAmount.objects.all()
    serializer_class = ItemsInitialAmountSerializer
  #  permission_classes = [IsAdminOrSupervisorOrStoreKeeper]

class TransactionsSerializerViewSet(viewsets.ModelViewSet):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer
   # permission_classes = [IsAdminOrStoreKeeper]

class ItemDateQtyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemDateQtySerializer
   # permission_classes = [IsAdminOrStoreKeeper]

class StockLedgerView(APIView):
    @extend_schema(responses={200: TransactionsSerializer(many=True)})
  #  permission_classes = [IsAdminOrSupervisorOrStoreKeeper]
    def get(self, request, format=None):
        item_id = request.query_params.get('item_id')
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        ledger_data = get_stock_ledger(item_id=item_id, start_date=start_date, end_date=end_date)
        return Response(ledger_data)