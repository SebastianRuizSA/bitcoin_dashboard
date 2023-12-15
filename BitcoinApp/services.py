import requests
from .models import Bitcoin

#Crear servicio que obtenga bitcoins de la api y luego los mande a la bd

def update_bitcoin_list():
    url = f'https://api.coingecko.com/api/v3/coins/list?include_platform=false'
    #url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=7"
    response = requests.get(url)
    data = response.json()
    #breakpoint()
    #bitcoin_list = data["bitcoins"]
    #breakpoint()

    return data

