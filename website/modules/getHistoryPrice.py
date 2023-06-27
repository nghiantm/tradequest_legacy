import yfinance as yf
import pandas as pd
import csv
import os
from datetime import date
import time
from multiprocessing.dummy import Pool as ThreadPool

def getHistory(symbol):
    # create a today variable to get today date
    today = date.today()

    # get the stock data
    stock = yf.Ticker(symbol)
    stock_data = stock.history(start="2000-01-01", end=today)

    # create a DataFrame with the stock data
    df = pd.DataFrame(stock_data, columns=['Open', 'High', 'Low', 'Close', 'Volume'])
    df = df.round(4)

    # save the DataFrame to a CSV file
    #file_name = ticker + '_data.csv'
    file_path = os.path.join(directory, ticker + 'data.csv')
    df.to_csv(file_path, index=True)
    return 0