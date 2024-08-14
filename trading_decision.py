import mysql.connector
from datetime import datetime
from forecaster import arima_analysis

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="missacm",
    password="1GreyrockPl!",
    database="market_data"
)
cursor = db.cursor()

# Create the 'optimiser_log' table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS optimiser_log (id INT AUTO_INCREMENT PRIMARY KEY, symbol VARCHAR(255), decision VARCHAR(50), timestamp DATETIME)")

def store_decision(symbol, decision):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    query = "INSERT INTO optimiser_log (symbol, decision, timestamp) VALUES (%s, %s, %s)"
    values = (symbol, decision, timestamp)
    cursor.execute(query, values)
    db.commit()

def trading_decision(forecast, symbol):
    current_price = forecast[0]
    next_price = forecast[1]
    
    if next_price > current_price:
        decision = 'Buy'
    elif next_price < current_price:
        decision = 'Sell'
    else:
        decision = 'Hold'
    
    store_decision(symbol, decision)
    
    return decision

# Example usage
symbol = 'IBM'
forecast = arima_analysis(symbol, '5min', 'your_api_key_here')
decision = trading_decision(forecast, symbol)
print(f'Trading Decision: {decision}')

# Close the database connection
cursor.close()
db.close()
