from django.urls import path
from .views import BitcoinViewSet, BitcoinUpdateViewSet, ValorHistoricoViewSet, ValorHistoricoUpdateViewSet

urlpatterns = [
    path('bitcoin/list/', BitcoinViewSet.as_view(), name='bitcoin-view'),
    path('bitcoin/update/', BitcoinUpdateViewSet.as_view(), name='bitcoin-update'),
    path('historical/list/', ValorHistoricoViewSet.as_view(), name='hv-view'),
    path('historical/update/', ValorHistoricoUpdateViewSet.as_view(), name='hv-update'),
]
