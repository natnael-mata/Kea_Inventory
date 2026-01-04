from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ItemsViewSet, ItemsStatusViewSet, ItemsListViewSet, ItemsPriceViewSet, ItemsInitialAmountViewSet, TransactionsSerializerViewSet, ItemDateQtyViewSet, StockLedgerView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemsViewSet)
router.register(r'items-status', ItemsStatusViewSet)
router.register(r'items-price', ItemsPriceViewSet)
router.register(r'items-initial-amount', ItemsInitialAmountViewSet)
router.register(r'transactions', TransactionsSerializerViewSet, basename='trans') 
router.register(r'items-list', ItemsListViewSet, basename='items-list')
router.register(r'item-date-qty', ItemDateQtyViewSet, basename='item-date-qty')

urlpatterns = [
    path('', include(router.urls)),
    path('stock-ledger/', StockLedgerView.as_view(), name='stock-ledger'),
]