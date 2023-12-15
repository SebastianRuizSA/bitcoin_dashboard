from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Bitcoin
from .serializers import BitcoinSerializer
from .selectors import bitcoin_list

class BitcoinViewSet(APIView):

    serializer_class = BitcoinSerializer
    queryset = Bitcoin.objects.all()

    def get(self, request):
        bitcoins = bitcoin_list()

        data = self.serializer_class(bitcoins, many=True).data

        return Response(data)