from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import BitcoinViewSet


router = DefaultRouter()
router.register(Bitcoin, BitcoinViewSet, base_name='bitcoin')

urlpatterns = [
    re_path('^', include(router.urls)),
]