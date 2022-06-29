import requests
import socket

API_key = "PYTER96QB79TYN3E"
URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=PYTER96QB79TYN3E'

r = requests.get(URL)
data = r.json()
print(data)
