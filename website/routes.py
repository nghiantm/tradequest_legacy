from flask import Blueprint, jsonify, render_template, request, redirect, flash, url_for, session
import json
import requests
import sqlite3
import csv

import json
import firebase_admin
from firebase_admin import credentials, auth, exceptions

from multiprocessing.dummy import Pool as ThreadPool

#For pulling market's data
import yfinance as yf

#For pulling history price
from datetime import date
import pandas as pd

routes = Blueprint("routes", __name__)

cred = credentials.Certificate("website/assets/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
#FIREBASE_WEB_API_KEY = os.environ.get("FIREBASE_WEB_API_KEY")
rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
#initialize userData for verifying
userData = []

@routes.route('/login', methods=['GET', 'POST'])
def login():
    global userData

    if request.method == 'POST':
        if request.form.get('signin') == 'clicked':
            #get data from form
            email = request.form['email']
            password = request.form['password']

            try:
                # Authenticate user with Firebase
                payload = json.dumps({
                    "email": email,
                    "password": password,
                    "returnSecureToken": True
                })

                userData = requests.post(rest_api_url,
                                  params={"key": "AIzaSyAW7rd5o-mbgMovc8K8D5md-u-JUeVoCcs"},
                                  data=payload)

                userData = userData.json()

                if 'idToken' in userData: #check if success signed in
                    print(userData) #print to console
                    return redirect(url_for('.simulator')) #redirect to ticker choose site
                else:
                    print(userData)
                    return redirect('#') #redirect to login site if fail

            except Exception as e:
                print(e)
                return redirect('#')


    return render_template('login.html', boolean=True)

@routes.route('/resetpassword', methods=['GET', 'POST'])
def reset_password():
    return render_template('resetpassword.html', boolean=True)

'''
@routes.route('/api/resetpassword', methods=['GET','POST'])
def api_reset_password():
    email = request.json['email']
    print(email)
    try:
        FBAuth.generate_password_reset_link(email)
        return jsonify({'message': 'Password reset link sent'}), 200
    except:
        return jsonify({'message': 'Unable to send password reset link'}), 400

'''

@routes.route('/logout')
def logout():
    global userData
    userData = []
    return redirect(url_for(".login"))


@routes.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        if request.form.get('signup') == 'clicked':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']

            try:
                #Create user
                user = auth.create_user(
                    email=email,
                    password=password,
                    display_name=username
                )

                return redirect(url_for('.login'))
            except Exception as e:
                #handle sign up error

                print(e)
                return render_template('signup.html', error=str(e))

    return render_template('signup.html')

@routes.route('/reset', methods=['GET', 'POST'])
def reset():
    return render_template('reset_request.html')


@routes.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html', boolean=True)

@routes.route('/about', methods=['GET', 'POST'])
def about():
    if request.form.get('about_page') == 'clicked':
        return redirect(url_for('.about'))
    if request.form.get('simulator_page') == 'clicked':
        return redirect(url_for('.simulator'))
    if request.form.get('recommend_page') == 'clicked':
        return redirect(url_for('.recommend'))

    return render_template('about.html', userData=userData)

@routes.route('/resources', methods=['GET', 'POST'])
def resources():
    return render_template('resources.html')

@routes.route('/price_volume', methods=['GET', 'POST'])
def price_and_volume():

    if request.method == 'POST':

        ticker = request.form['ticker']

        # create a today variable to get today date
        today = date.today()

        # get the stock data
        stock = yf.Ticker(ticker)
        stock_data = stock.history(start="2000-01-01", end=today)

        # create a DataFrame with the stock data
        df = pd.DataFrame(stock_data, columns=['Open', 'High', 'Low', 'Close', 'Volume'])
        df = df.round(4)

        # save the DataFrame to a CSV file
        file_name = ticker + '_data.csv'
        df.to_csv(file_name, index=True)

        # read the CSV file and store its contents in a variable
        data = pd.read_csv(file_name).to_dict('records')

        # render the template with the data passed to it
        return render_template('output.html', data=data)

    return render_template('price_volume.html')

@routes.route('/simulator', methods=['GET', 'POST'])
def simulator():
    if userData == None or 'idToken' not in userData:
        return redirect(url_for(".login"))
    else:
        if request.form.get('about_page') == 'clicked':
            return redirect(url_for('.about'))
        if request.form.get('simulator_page') == 'clicked':
            return redirect(url_for('.simulator'))
        if request.form.get('recommend_page') == 'clicked':
            return redirect(url_for('.recommend'))
        if request.form.get('signout') == 'clicked':
            return redirect(url_for('.logout'))

        if request.form.get('start') == 'clicked':
            input_symbol = request.form['stock_symbol']
            input_symbol = input_symbol.upper()
            symbol_error = 1
            with open('website/assets/nasdaq-100.csv') as csv_file_input:
                csv_reader = csv.reader(csv_file_input, delimiter=',')
                for row in csv_reader:
                    if input_symbol == row[0]:
                        symbol_error = 0
                        csv_file_input.close()
                        return redirect(url_for('.trading', symbol=input_symbol))
            return render_template('simulator.html', symbol_error=symbol_error, userData=userData)
        return render_template('simulator.html', userData=userData)


#TEST, DON'T TOUCH
@routes.route('/trading', methods=['GET', 'POST'])
def trading():
    if 'idToken' not in userData:
        return redirect(url_for(".login"))
    else:    
        if request.form.get('about_page') == 'clicked':
            return redirect(url_for('.about'))
        if request.form.get('simulator_page') == 'clicked':
            return redirect(url_for('.simulator'))
        if request.form.get('recommend_page') == 'clicked':
            return redirect(url_for('.recommend'))

        stock_symbol = request.args.get('symbol')
        chart_symbol = f'NASDAQ:{stock_symbol}'

        # pull prices
        stock = yf.Ticker(stock_symbol)
        market_price = stock.history(period="1d")["Close"][0]

        filename = f'website/assets/buy_sell/{stock_symbol}.csv'

        #if csv empty, initialize with a blank transaction
        with open(filename, mode='a') as csv_file_output:
            csv_writer = csv.writer(csv_file_output, delimiter=';')
            with open(filename, mode='a+') as csv_file_input:
                csv_reader = csv.reader(csv_file_input, delimiter=';')
                if not any(csv_reader):
                    csv_writer.writerow(['test', 0, 0])
            csv_file_input.close()
        csv_file_output.close()
        
        #calculate stats
        with open(filename, mode='r') as csv_file_input:
            # open and read csv file to get cost and volume bough
            csv_reader = csv.reader(csv_file_input, delimiter=';')
            total_cost = 0
            total_volume = 0
            total_value = 0
            profit = 0
            profit_percent = 0
            if any(csv_reader):
                for row in csv_reader:
                    # index: 0 = date, 1 = buying price, 2 = volume
                    total_volume += int(row[2])
                    total_cost += float(row[1])*int(row[2])
                    total_value += market_price*int(row[2])
                profit = total_value - total_cost
                if total_cost > 0:
                    profit_percent = (profit/total_cost)*100
                csv_file_input.close()
            else:
                pass
        csv_file_input.close()

        shares_error = 0
        if request.method == 'POST':
            with open(filename, mode='a') as csv_file_output:
                # open and write csv file
                csv_writer = csv.writer(csv_file_output, delimiter=';')
                volume = 0

                if request.form.get('buy') == 'clicked':
                    volume = int(request.form['volume-input'])
                    if volume < 0:
                        shares_error = "Invalid shares number"
                    else:
                        csv_writer.writerow(['test', market_price, volume])
                        csv_file_input.close()
                        #reload the page
                        return redirect('#')
                    
                if request.form.get('sell') == 'clicked':
                    volume = int(request.form['volume-input'])
                    if volume > total_volume or volume < 0:
                        shares_error = "Invalid shares number"
                    else:
                        csv_writer.writerow(['test', market_price, -volume])
                        csv_file_input.close()
                        #reload the page
                        return redirect('#')
            csv_file_output.close()  
        return render_template('trading.html', total_cost=total_cost, total_volume=total_volume, 
                            market_price=market_price, total_value=total_value, profit=profit, 
                            profit_percent=profit_percent, shares_error=shares_error, stock_symbol=stock_symbol, chart_symbol=chart_symbol, userData=userData)

@routes.route('/price_board', methods=['GET', 'POST'])
def price_board():
    with open("website/assets/sp500_companies.csv", 'r') as sp500:
        symbolReader = csv.reader(sp500)
        #skip header line
        next(symbolReader)
        #initialize a symbol list
        symbolName = []
        for line in symbolReader:
            symbolName.append(line[0])
        sp500.close()
    symbolName.sort()

    #loop through all symbol, create stock object, then append into a list
    def fetch_price(stockObjects):
        global closePrice
        closePrice = []
        try:
            closePrice.append(round(stockObjects.history(period="1d")["Close"][0],2))
        except:
            closePrice.append(None)
        return

    return render_template('price_board.html', symbolName=symbolName)

@routes.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if 'idToken' not in userData:
        return redirect(url_for(".login"))
    else:    
        if request.form.get('about_page') == 'clicked':
            return redirect(url_for('.about'))
        if request.form.get('simulator_page') == 'clicked':
            return redirect(url_for('.simulator'))
        if request.form.get('recommend_page') == 'clicked':
            return redirect(url_for('#'))
        return render_template('recommend.html', userData=userData)