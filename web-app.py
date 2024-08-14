from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="missacm",
    password="1GreyrockPl!",
    database="market_data"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def display_trading_log():
    # Query trading decisions from the MySQL table
    query = "SELECT symbol, decision, timestamp FROM optimiser_log ORDER BY timestamp DESC"
    cursor.execute(query)
    trading_log = cursor.fetchall()
    
    return render_template('trading_log.html', trading_log=trading_log)

if __name__ == '__main__':
    app.run(debug=True)
