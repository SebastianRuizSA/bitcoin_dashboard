from .models import Bitcoin

def bitcoin_list() -> Iterable[User]:

    query = Q(id__in=user_ids) #Que esten en una fecha especifica

    return Bitcoin.objects.filter(query)