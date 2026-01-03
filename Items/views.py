from rest_framework import viewsets
from .models import Items, Category, Items_Status
from .serializers import ItemsSerializer, CategorySerializer, ItemsStatusSerializer, ItemReportSerializer
class CategoryViewSet(viewsets.ModelViewSet):   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ItemsViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

class ItemsListViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.select_related('category').all()
    serializer_class = ItemReportSerializer


class ItemsStatusViewSet(viewsets.ModelViewSet):
    queryset = Items_Status.objects.all()
    serializer_class = ItemsStatusSerializer
   
    