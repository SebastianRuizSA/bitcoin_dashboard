import requests
from django.db import transaction
from .models import Bitcoin, ValorHistorico
from datetime import datetime

#Los servicios se comunican con la API y guardan los datos en la BD.

def get_bitcoins_list_from_API():
    url = f'https://api.coingecko.com/api/v3/coins/list?include_platform=false'
    response = requests.get(url)
    data = response.json()
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

def convert_unix_timestamp_to_datetime(unix_timestamp, format='%Y-%m-%d'):
    """
    Convert a Unix timestamp to a formatted date string.

    Parameters:
    - unix_timestamp (float or int): The Unix timestamp.
    - format (str): The desired date format. Default is '%Y-%m-%d'.

    Returns:
    - str: The formatted date string.
    """
    converted_datetime = datetime.utcfromtimestamp(unix_timestamp)
    formatted_date = converted_datetime.strftime(format)
    return formatted_date


def get_historic_values_list_from_API(bitcoin_id, currency, start_date, end_date):
    # Transformar las fechas a datetime.

    start_date = datetime.strptime(start_date, "%d-%m-%Y")
    end_date = datetime.strptime(end_date, "%d-%m-%Y")

    # Calculate the difference between the two dates
    days = (start_date - end_date).days

    url = f'https://api.coingecko.com/api/v3/coins/{bitcoin_id}/market_chart?vs_currency={currency}&days={days}'
    response = requests.get(url)
    data = response.json()
    return data

@transaction.atomic
def update_valor_historico_list(bitcoin_id, currency, start_date, end_date):
    historic_values = get_historic_values_list_from_API(bitcoin_id, currency, start_date, end_date)
    btc = Bitcoin.objects.get(id = bitcoin_id)
    for hv in historic_values:
        day = convert_unix_timestamp_to_datetime(hv["day_timestamp"])
        valor = ValorHistorico(
            btc = btc,
            day = day,
            price = hv["price"],
            marketcap = hv["marketcap"]
        )
        valor.full_clean()
        valor.save()

    return historic_values