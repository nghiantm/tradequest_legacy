import csv
import math
import pandas as pd

start = '2010-01-04 00:00:00-04:00'

capital = 1000
stock = 0
bought = False

df = pd.read_csv('stock_prices_with_EMA.csv', index_col=0)

df = df.drop(df.index[:start])

for index, row in df.iterrows():
    count = 0
    lastClose = row['Close']
    if bought == False: 
        if row['5EMA'] > row['23EMA']:
            if row['200EMA'] < row['Close']:
                stock += math.floor(capital/row['Close'])
                print(f"Bought {stock} at {row['Close']} in {index}")
                capital -= stock*row['Close']
                bought = True
                count += 1
    elif bought == True:
        if row['Close'] < row['100EMA']:
            capital += stock*row['Close']
            print(f"Sold {stock} at {row['Close']} in {index}")
            stock = 0
            bought = False
            count += 1
'''
with open('stock_prices_with_EMA.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')

    #skip header row
    next(reader)

    #5=6, 23=7, 100=8, 200=9, close=4
    count = 0
    for row in reader:
        lastClose = float(row[4])
        if bought == False:
            if float(row[6]) > float(row[7]):
                if float(row[9]) < float(row[4]):
                    stock += math.floor(capital/float(row[4]))
                    print("Bought", stock)
                    capital -= stock*float(row[4])
                    bought = True
                    count += 1
        elif bought == True:
            if float(row[4]) < float(row[8]):
                capital += stock*float(row[4])
                print("Sold")
                stock = 0
                bought = False
                count += 1
    f.close()
'''

print("Total Capital Left: ", capital)
print("Total Stock: ", stock)
print("Total Value:", stock*lastClose + capital)
print("DEBUG COUNT:", count)