from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KanbanViewSet

router = DefaultRouter()
router.register(r'kanbans', KanbanViewSet, basename='kanbans')

urlpatterns = router.urls