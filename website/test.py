import csv
import yfinance as yf
import time
from multiprocessing.dummy import Pool as ThreadPool

start = time.time()

def fetchMarketPrice(stockObjects, symbolName):
    try:
        return symbolName,round(stockObjects.history(period="1d")["Close"][0],2)
    except:
        return None

def fetchOpenPrice(stockObjects, symbolName):
    try:
        return symbolName,round(stockObjects.history(period="1d")["Open"][0],2)
    except:
        return None

def fetchHighPrice(stockObjects, symbolName):
    try:
        return symbolName,round(stockObjects.history(period="1d")["High"][0],2)
    except:
        return None

def fetchLowPrice(stockObjects, symbolName):
    try:
        return symbolName,round(stockObjects.history(period="1d")["Low"][0],2)
    except:
        return None

def fetchVolume(stockObjects, symbolName):
    try:
        return symbolName,round(stockObjects.history(period="1d")["Volume"][0],2)
    except:
        return None

def pullMarket(fetchMarketPrice, stockObjects, symbolName):
    nasdaq100Market = []
    pool = ThreadPool(4)
    nasdaq100Market.append(pool.starmap(fetchMarketPrice, zip(stockObjects, symbolName)))
    pool.close()
    pool.join()
    nasdaq100Market.sort()
    return nasdaq100Market

def pullOpen(fetchOpenPrice, stockObjects, symbolName):
    nasdaq100Open = []
    pool = ThreadPool(4)
    nasdaq100Open.append(pool.starmap(fetchOpenPrice, zip(stockObjects, symbolName)))
    pool.close()
    pool.join()
    nasdaq100Open.sort()
    return nasdaq100Open


with open("/Users/Nghia/Desktop/CI102/stock-trading-simulator/website/assets/nasdaq-100.csv", 'r') as n100:
    symbolReader = csv.reader(n100)
    #skip header line
    next(symbolReader)
    #initialize a symbol list
    symbolName = []
    for line in symbolReader:
        if len(line[0]) < 5:
            symbolName.append(line[0])
        else:
            pass
    n100.close()
symbolName.sort()

stockObjects = []
for symbol in symbolName:
    stock = yf.Ticker(symbol)
    stockObjects.append(stock)

nasdaq100Market = pullMarket(fetchMarketPrice, stockObjects, symbolName)
#nasdaq100Open = pullOpen(fetchOpenPrice, stockObjects, symbolName)

'''

nasdaq100Market = []
nasdaq100Open = []
nasdaq100High = []
nasdaq100Low = []
nasdaq100Volume = []

    pool = ThreadPool(5)

nasdaq100Market.append(pool.starmap(fetchMarketPrice, zip(stockObjects, symbolName)))
nasdaq100Open.append(pool.starmap(fetchOpenPrice, zip(stockObjects, symbolName)))
nasdaq100High.append(pool.starmap(fetchHighPrice, zip(stockObjects, symbolName)))
nasdaq100Low.append(pool.starmap(fetchLowPrice, zip(stockObjects, symbolName)))
nasdaq100Volume.append(pool.starmap(fetchVolume, zip(stockObjects, symbolName)))

pool.close()
pool.join()

nasdaq100Market.sort()
nasdaq100Open.sort()
nasdaq100High.sort()
nasdaq100Low.sort()
nasdaq100Volume.sort()
'''

end = time.time()
elapse = end - start

print(nasdaq100Market)
#print(nasdaq100Open)

'''
print(nasdaq100Open)
print(nasdaq100High)
print(nasdaq100Low)
print(nasdaq100Volume)
'''

print("DEBUG:", elapse)