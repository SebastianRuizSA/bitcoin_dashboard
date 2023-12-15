import requests
from django.db import transaction
from .models import Bitcoin

#Los servicios se comunican con la API y guardan los datos en la BD.

def get_bitcoins_list_from_API():
    url = f'https://api.coingecko.com/api/v3/coins/list?include_platform=false'
    response = requests.get(url)
    data = response.json()
    # Hacer algo para que la data se guarde en un archivo en vez de pedirla a cada rato.
    return data

@transaction.atomic
def update_bitcoin_list():
    bitcoins = get_bitcoins_list_from_API()
    for bitcoin in bitcoins:
        payment = Bitcoin(
            id = bitcoin["id"],
            symbol = bitcoin["symbol"],
            name = bitcoin["name"]
        )
        payment.full_clean()
        payment.save()

    return bitcoins

