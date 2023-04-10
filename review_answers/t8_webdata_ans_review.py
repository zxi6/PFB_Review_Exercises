#----------- 1. Write a program to retrieve the foreign exchange rate (forex) from https://app.getexchangr.com -----------#

# Find out what is the exchange rate of SGD1.00 (Singapore Dollar) to US Dollars (USD), Canadian Dollars (CAD) and Euro (EUR) 
# You will need an API key from exchangr for this to work.
# To ease your tasks, you can simply execute the code below with these API endpoints and query parameters:

# import requests and json module 
import requests, json

# API Endpoints
API_KEY = "612q5e02ebb2403738ks3yv1680rc4ya0h2c24l52nc8q33qgb875xpb0z7f"
base = "SGD"
symbols = "USD,CAD,EUR"
data = "2022-08-24"

# Exchangr API URL with end points using f-strings
url = f"https://app.getexchangr.com/api/{date}?access_key={API_KEY}&base={base}&symbols={symbols}"

# get the data using .get() from request library
response = requests.get(url)
# print the url to check if the endpoints are correct.
print(response.url)
# print the status code after .get(), a return of 200 imply a successful API connection
print(response.status_code)
# print the data retrieved as json
print(response.json())

#----------- 2. Arrange the data in json format more readable  -----------#

# store the json data to a variable
forex_data = response.json()
# use .dumps() from json module to pretty print the data
print(json.dumps(forex_data, indent=4))

# When the data is printed, it should look like the followings:
"""
SGD1 = CAD0.9304781317645886 on 2022-08-24
SGD1 = EUR0.7189482270473462 on 2022-08-24
SGD1 = USD0.7166906514951366 on 2022-08-24
"""

# extract the date from forex_data variable
date = forex_data["data"]["date"]
# extract the base currency from forex_data variable
base_currency = forex_data["data"]["base"]
# extract the symbols and exchange rate from forex_data variable
forex_currency = forex_data["data"]["rates"]

# YOUR TASKL use a for loop to print the variables in f-strings.
for forex in forex_currency:
    print(f"{base}1 =  {forex}{forex_currency[forex]} on {date}")





