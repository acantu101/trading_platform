
import requests

def fetch_intraday_data(symbol, interval, apikey, function='TIME_SERIES_INTRADAY', adjusted=True, extended_hours=True, month=None, outputsize='compact', datatype='json'):
    if function == 'TIME_SERIES_INTRADAY':
        url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval={interval}&apikey={apikey}'
    else:
        base_url = 'https://api.example.com/intraday_data'  # Replace with the actual API endpoint
        params = {
            'function': function,
            'symbol': symbol,
            'interval': interval,
            'adjusted': adjusted,
            'extended_hours': extended_hours,
            'month': month,
            'outputsize': outputsize,
            'datatype': datatype,
            'apikey': apikey
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Failed to fetch data. Status Code: {response.status_code}')
            return None

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Failed to fetch data. Status Code: {response.status_code}')
        return None
