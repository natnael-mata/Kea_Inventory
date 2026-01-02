from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ItemsViewSet, ItemsStatusViewSet, ItemsStatusCreateViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'items', ItemsViewSet)
router.register(r'items-status', ItemsStatusViewSet)
router.register(r'items-status-create', ItemsStatusCreateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]