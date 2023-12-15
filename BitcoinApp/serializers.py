from rest_framework.serializers import ModelSerializer
from .models import Bitcoin, ValorHistorico

class BitcoinSerializer(ModelSerializer):
    class Meta:
        model = Bitcoin
        fields = '__all__'

class ValorHistoricoSerializer(ModelSerializer):
    class Meta:
        model = ValorHistorico
        fields = '__all__'