from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Bitcoin
from .serializers import BitcoinSerializer, ValorHistoricoSerializer
from .selectors import get_bitcoin_list
from .services import update_bitcoin_list

class BitcoinViewSet(APIView):

    serializer_class = BitcoinSerializer

    def get(self, request):
        queryset = get_bitcoin_list()
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

class BitcoinUpdateView(APIView):

    serializer_class = BitcoinSerializer

    def get(self, request):
        bitcoins = update_bitcoin_list()
        data = self.serializer_class(bitcoins, many=True).data
        return Response(data)

class ValorHistoricoViewSet(APIView):

    serializer_class = ValorHistoricoSerializer

    def get(self, request):
        queryset = get_bitcoin_list()
        data = self.serializer_class(queryset, many=True).data
        return Response(data)