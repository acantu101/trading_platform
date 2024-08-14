# Trading Pipeline README

This trading pipeline consists of four main components: **Market Data App**, **Forecaster App**, **Optimizer App**, and a **Flask Web Application** for displaying the trading decisions log.

## Components:
1. **Market Data App**:
   - Responsible for fetching intraday stock data from an API endpoint.
   - Uses the `fetch_intraday_data` function to retrieve data based on the symbol, interval, and API key.
   
2. **Forecaster App**:
   - Utilizes the retrieved data to perform ARIMA analysis for forecasting stock prices.
   - The `arima_analysis` function generates a forecast based on the provided symbol, interval, and API key.
   
3. **Optimizer App**:
   - Makes trading decisions based on the forecasted prices from the Forecaster app.
   - Connects to a MySQL database to store trading decisions in the `optimiser_log` table.
   
4. **Flask Web Application**:
   - Displays the historical trading log stored in the MySQL database.
   - The web app connects to the database to fetch and present the trading decisions log.

## Setup Instructions:
1. Install the required Python libraries:
   
pip install requests pandas statsmodels Flask Flask-MySQLdb mysql-connector-python

code



2. **Database and Table Creation:**
   - Create a database named `market_data` using the following SQL command:
     
sql CREATE DATABASE market_data;

code


   - Switch to the `market_data` database:
     
sql USE market_data;

code


   - Create a table named `optimiser_log` with columns: `id` (INT, AUTO_INCREMENT, PRIMARY KEY), `symbol` (VARCHAR), `decision` (VARCHAR), `timestamp` (DATETIME):
     
sql CREATE TABLE optimiser_log ( id INT AUTO_INCREMENT PRIMARY KEY, symbol VARCHAR(255), decision VARCHAR(50), timestamp DATETIME );

code



3. Update the MySQL credentials, API URL, and API key in the respective app scripts.

## Usage:
1. Run the Flask web application by executing `python web_app.py`.
2. Access the web app in a browser at `http://127.0.0.1:5000/` to view the trading log.
3. Execute the Optimizer app script to generate trading decisions based on the forecasted prices.

Feel free to customize and expand the functionality of each component as needed for your trading pipeline.

---

This README provides an overview of the trading pipeline components, setup instructions, and usage guidelines. Adjust the instructions based on the specifics of your implementation and requirements.
You can copy and paste this markup content into your README file for the trading pipeline documentation.
