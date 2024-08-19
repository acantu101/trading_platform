from flask import Flask, render_template, request
import mysql.connector
from market_data import fetch_intraday_data
from forecaster import arima_analysis
from optimizer import trading_decision

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="missacm",
    password="1GreyrockPl!",
    database="market_data"
)
cursor = db.cursor(dictionary=True)

@app.route('/', methods=['GET', 'POST'])
def process_trading_data():
    if request.method == 'POST':
        symbol = request.form['symbol']  # Extract the symbol parameter from the form submission

        # Call the Market Data App script to fetch intraday data
        intraday_data = fetch_intraday_data(symbol, interval='5min', apikey='your_api_key_here')

        # Call the Forecaster App script to perform ARIMA analysis
        forecast = arima_analysis(symbol, interval='daily')

        # Call the Optimizer App script to make trading decisions
        decision = trading_decision(forecast)

        # Store the trading decision in the MySQL database
        # Add code to insert the decision into the optimiser_log table

    # Query trading decisions from the MySQL table
    query = "SELECT symbol, decision, timestamp FROM optimiser_log ORDER BY timestamp DESC"
    cursor.execute(query)
    trading_log = cursor.fetchall()

    return render_template('trading_log.html', trading_log=trading_log, intraday_data=intraday_data, forecast=forecast, decision=decision)

if __name__ == '__main__':
    app.run(debug=True)

