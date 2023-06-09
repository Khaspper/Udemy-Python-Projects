import math
import requests
import datetime as dt
from newsapi import NewsApiClient
from twilio.rest import Client
from pprint import pprint
# * The bottom are to import env variables
import os
from dotenv import load_dotenv
load_dotenv("/Users/khaspper/Documents/code/python/.env")

STOCK = "PLTR"
COMPANY_NAME = "Tesla Inc"

twillio_account_sid = os.getenv("twilio_account_sid")
twillio_auth_token = os.getenv("twilio_auth_token")

# * Step 1 Get the stock prices that we are interested in it pulls in the chosen stock's yesterday closing price and
# * then the previous day's closing price then compare the two and determine if the stock is down or up
# * then get the percentage of the comparison

# * Then get the relevant news

# * Send the Sms about what's happening to the stock

AV_endpoint = "https://www.alphavantage.co/query"
av_api_key = os.getenv("AV_api_key")
news_api_key = os.getenv("NEWS_api_key")

parameters = {
    "apikey": av_api_key,
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
}

stock_response = requests.get(AV_endpoint, params=parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

# * Getting yesterday's date and the day before yesterday's (ereyesterday) date
# * sunday (6) monday (0)

# * I want to get the week day and make sure it is not a weekend
days_to_subtract = 1
while True:
    previous_day = (dt.datetime.now() - dt.timedelta(days=days_to_subtract)).date()
    if previous_day.weekday() < 5:
        break
    days_to_subtract += 1

while True:
    ereyesterday = (dt.datetime.now() - dt.timedelta(days=days_to_subtract)).date()
    if previous_day.weekday() < 5 and ereyesterday != previous_day:
        break
    days_to_subtract += 1

# * Get the previous days' closing price
previous_day_close = float(stock_data[f"{previous_day}"]["4. close"])
ereyesterday_close = float(stock_data[f"{ereyesterday}"]["4. close"])

# * Determine if the stock is going up or down
if (previous_day_close - ereyesterday_close) > 0:
    arrow = "🔺"
    percentage = math.floor(((previous_day_close - ereyesterday_close) / previous_day_close) * 100)
    is_up = True
else:
    arrow = "🔻"
    percentage = math.floor(((ereyesterday_close - previous_day_close) / ereyesterday_close) * -100)
    is_up = False

# if percentage >= 5:
newsapi = NewsApiClient(api_key=os.getenv("NEWS_api_key"))
top_headlines = newsapi.get_everything(q=STOCK)
formatted_articles = []
for _ in range(0, 3):
    formatted_articles.append(f'\n{STOCK}: {arrow}{percentage}%\nHeadline: {top_headlines["articles"][_]["title"]}'
                              f'\nBrief: {top_headlines["articles"][_]["description"]}')

for num in range(3):
    pprint(f'Content: {top_headlines["articles"][num]["content"]}')
    pprint(f'Description: {top_headlines["articles"][num]["description"]}')
    print("\n\n")

    # client = Client(twillio_account_sid, twillio_auth_token)
    # for article in formatted_articles:
    #     message = client.messages\
    #         .create(
    #         body=article,
    #         from_=os.getenv("twilio_phone_num"),
    #         to=os.getenv("my_phone_num")
    #     )
    # print(message.status)
