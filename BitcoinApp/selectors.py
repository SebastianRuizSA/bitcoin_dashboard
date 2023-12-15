from .models import Bitcoin, ValorHistorico
from django.db.models import Q

# Los selectores hacen consultas a la BD dependiendo de los filtros.

def get_bitcoin_list():
    return Bitcoin.objects.all() # Retorna todos los objetos bitcoin

def get_historic_value_list(start_date, end_date): # Valores Historicos dependen de la fecha que se agrega
    query = Q(day__range=(start_date, end_date)) #Que esten en una fecha especifica
    return ValorHistorico.objects.filter(query) # Retorna todos los objetos bitcoin