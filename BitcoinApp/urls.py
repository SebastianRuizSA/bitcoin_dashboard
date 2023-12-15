from django.urls import path, include
from rest_framework import routers
from .views import BitcoinUpdateView

#router = routers.DefaultRouter()
#router.register(r'update', BitcoinUpdateView)

urlpatterns = [
    #path('', include(router.urls)),
    path('update/', BitcoinUpdateView.as_view(), name='bitcoin-update'),

]