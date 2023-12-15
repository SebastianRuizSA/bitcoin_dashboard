from rest_framework.serializers import ModelSerializer

from .models import Bitcoin

class BitcoinSerializer(ModelSerializer):
    class Meta:
        model = Bitcoin
        fields = (
            'id', 'id_btc', 'symbol', 'name'
        )