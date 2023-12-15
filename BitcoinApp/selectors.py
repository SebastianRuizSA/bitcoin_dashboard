from .models import Bitcoin
from django.db.models import Q


def get_bitcoin_list(): #-> Iterable[User]:

    #query = Q(id__in=user_ids) #Que esten en una fecha especifica

    return Bitcoin.objects.all() # Retorna todos los objetos bitcoin
