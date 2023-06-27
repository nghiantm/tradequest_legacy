## Trade Quest ##

## Overview and goals ##
Our Stock Trading Simulator Website is a platform that allows users to simulate stock trading without risking real money. Users can buy and sell stocks, track their portfolios, and view real-time stock prices. The website has been developed using Flask and uses Firebase as a database hosting service. Some of the benefits of our website are:

Users can practice trading without risking real money
Users can track their portfolios and analyze their trading strategies
Users can view real-time stock prices and market news

## Target Audience ##
The target audience for our Stock Trading Simulator Website is anyone who wants to learn about stock trading or practice trading without risking real money. The website is ideal for:

-Beginner traders who want to learn about the stock market
-Experienced traders who want to test their trading strategies
-Investors who want to track their portfolios and analyze their performance

## Purpose of The Guide ##
The purpose of this guide is to provide users with the information they need to effectively use the system

## Contributors ##
- Neil Luong
- Matt Nguyen
- Bobby Nguyen
- Benji Bui
- Shaan Singh

## System Manual ##

## Minimum hardware and software requirements:
- Computer with internet access
- Web brower(Chrome, FireFox, Safari,...)
## Installation Guide
In order to run this website, you need:
1/ Python3
2/ install Flask: (run this in the terminal)
    - pip install flask
    - pip install flask-login
    - pip install flask-sqlalchemy
3/ install the requirements:
    - pip install -r requirements.txt
    - pip install yfinance
4/ get the service account key:
    - the file containing the key is named: "serviceAccountKey.json" 
    - this file can only be given by asking the creators and co-creators of this project (for security purposes)
    - send an email to "luongdminh183@gmail.com" if you are a new member of this team and needs the key to develop the project

*That should get the website up and running
if not, please contact the email above for more information.

## Explanations of error messages and troubleshooting guides
1/  Error Message: "Invalid login credentials."
    Cause: This error message appears when you enter incorrect login credentials (i.e., username or password).

    Troubleshooting: Ensure that you have entered the correct username and password. Check that your caps lock key is not on and that you have entered your login information correctly. If you are still unable to log in, click the "Forgot Password" button to reset your password.

2/  Error Message: "Server Error."
    Cause: This error message appears when there is a problem with the server.

    Troubleshooting: Wait a few minutes and try again. If the problem persists, contact our support team for assistance.

3/  Error Message: "Stock Not Found."
    Cause: This error message appears when you search for a stock that does not exist in our database.

    Troubleshooting: Double-check the spelling of the stock name and ensure that you are searching for the correct stock symbol. If the stock still cannot be found, it may not be available for trading on our platform.

If you encounter any other error messages or issues while using our Stock Trading Simulator Website, please contact our support team for assistance.

## Contact Developers
If you have any questions or issues with our Stock Trading Simulator Website that are not addressed in this system guide or the troubleshooting section, please do not hesitate to contact our support team for assistance. You can reach us through email at: 
- luongdminh183@gmail.com


## User Guide ##
This user guide provides instructions on how to effectively use the system and its various features. It covers topics such as system startup, feature usage, visual references with screenshots, and example inputs and outputs.
## How to Start the System 
- Ensure that you have downloaded all the requirements in the Installation Guide
- Go to the file main.py and run that file
- Once it ran, a link will appear under the terminal assuming everything works perfectly
- Click on the link and it will lead you to the website
          
## How to use the key features of the system 
Step 1:
- Go to the sign up page and enter all the required information and register for an account
- After that, it will automatically redirect you to the login page, type in your info and you have entered the website

Step 2:
- Enter your stock symbol. If you dont know any stock symbol, just click on " Dont know yours?"
- Click on "Start trading"
- Then the stock will appear and you have two options: buy or sell
- Information about the stock current price will be updated everytime you reload the page and the volume of your stock will also be displayed



## Example inputs and outputs 
To provide you with a better understanding of how the system works, here are some example inputs and their corresponding outputs:

Example 1:
- Input: TSLA into the stock symbol bar
- Output: WHole Tesla stock market with graphs, current market price, current volume, current portfolio value, and current profit

Example 2:
- Input: username, email, password in the signup page
- Output: leads to login page







