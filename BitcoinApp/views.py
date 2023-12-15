from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Bitcoin
from .serializers import BitcoinSerializer
from .selectors import get_bitcoin_list
from .services import update_bitcoin_list

class BitcoinViewSet(APIView):

    serializer_class = BitcoinSerializer
    queryset = Bitcoin.objects.all()

    def get(self, request):
        bitcoins = get_bitcoin_list()

        data = self.serializer_class(bitcoins, many=True).data

        return Response(data)

class BitcoinUpdateView(APIView):

    serializer_class = BitcoinSerializer

    def get(self, request):
        users = update_bitcoin_list()

        breakpoint()

        data = self.serializer_class(users, many=True).data

        return Response(data)