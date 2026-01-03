from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ItemsViewSet, ItemsStatusViewSet, ItemsListViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemsViewSet)
router.register(r'items-list', ItemsListViewSet, basename='items-list')
router.register(r'items-status', ItemsStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
]