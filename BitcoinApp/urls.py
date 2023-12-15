from django.urls import path
from .views import BitcoinViewSet, BitcoinUpdateView

urlpatterns = [
    path('', BitcoinViewSet.as_view(), name='bitcoin-view'),
    path('update/', BitcoinUpdateView.as_view(), name='bitcoin-update'),
]