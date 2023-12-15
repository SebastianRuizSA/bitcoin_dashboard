from .models import Bitcoin, ValorHistorico
from django.db.models import Q

# Los selectores hacen consultas a la BD dependiendo de los filtros.

def get_bitcoin_list():

    return Bitcoin.objects.all() # Retorna todos los objetos bitcoin

def get_valor_historico_list(): # Valores Historicos dependen de la fecha que se agrega

    query = Q(id__in=user_ids) #Que esten en una fecha especifica

    return ValorHistorico.objects.filter(query) # Retorna todos los objetos bitcoin