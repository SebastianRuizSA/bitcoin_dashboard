from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets
from datetime import datetime

from .models import Bitcoin
from .serializers import BitcoinSerializer, ValorHistoricoSerializer
from .selectors import get_bitcoin_list, get_historic_value_list
from .services import update_bitcoin_list, update_valor_historico_list

class BitcoinViewSet(APIView):

    serializer_class = BitcoinSerializer

    def get(self, request):
        queryset = get_bitcoin_list()
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

class BitcoinUpdateViewSet(APIView):

    serializer_class = BitcoinSerializer

    def get(self, request):
        bitcoins = update_bitcoin_list()
        data = self.serializer_class(bitcoins, many=True).data
        return Response(data)

class ValorHistoricoViewSet(APIView):

    serializer_class = ValorHistoricoSerializer

    def get(self, request):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")

        queryset = get_historic_value_list(start_date, end_date)
        data = self.serializer_class(queryset, many=True).data
        return Response(data)

class ValorHistoricoUpdateViewSet(APIView):

    serializer_class = ValorHistoricoSerializer

    def get(self, request):
        bitcoin_id = request.GET.get('bitcoin_id')
        currency = request.GET.get('currency')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        historic_values = update_valor_historico_list(bitcoin_id, currency, start_date, end_date)
        data = self.serializer_class(historic_values, many=True).data
        return Response(data)