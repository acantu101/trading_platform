import mysql.connector
import pandas as pd
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA
from market_data import fetch_intraday_data

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="missacm",
    password="1GreyrockPl!",
    database="market_data"
)
cursor = db.cursor()

def arima_analysis(symbol, interval, apikey, function='TIME_SERIES_INTRADAY'):
    intraday_data = fetch_intraday_data(symbol, interval, apikey, function=function)
    
    if not intraday_data:
        print('Failed to fetch intraday data. Exiting analysis.')
        return None
    
    intraday_df = pd.DataFrame(intraday_data['time_series'])  # Assuming 'time_series' key in response
    intraday_df['timestamp'] = pd.to_datetime(intraday_df['timestamp'])
    intraday_df.set_index('timestamp', inplace=True)
    intraday_df = intraday_df.resample('1H').mean()
    
    model = ARIMA(intraday_df['price'], order=(1, 1, 1))
    model_fit = model.fit()
    
    forecast = model_fit.forecast(steps=10)
    
    return forecast

# Example usage
symbol = 'IBM'
apikey = 'your_api_key_here'
forecast = arima_analysis(symbol, '5min', apikey)
if forecast:
    print(f'Forecasted prices: {forecast}')

# Close the database connection
cursor.close()
db.close()
