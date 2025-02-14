import requests
import os
from dotenv import load_dotenv
from datetime import date, timedelta
from twilio.rest import Client

load_dotenv(r"C:\fakepath\.env")
NEWS_APIKEY = os.getenv("news_api_key")
AV_APIKEY = os.getenv("alphavantage_api_key")
TWILIO_account_sid = os.getenv("twilio_account_sid")
TWILIO_auth_token = os.getenv("twilio_auth_token")

STOCK = "ILMN"
COMPANY_NAME = "Illumina Inc"
TODAY = date.today()
YESTERDAY = TODAY - timedelta(days = 1)
DAY_BEFORE_YESTERDAY = TODAY - timedelta(days = 2)
symbol = ""

# Calculate STOCK price increase/decreases by 5% between yesterday and the day before yesterday

stock_url = "https://www.alphavantage.co/query?"
stock_parameters = {"function": "TIME_SERIES_DAILY",
                    "symbol": STOCK,
                    "outputsize": "compact",
                    "apikey": AV_APIKEY,
                    }

AV_response = requests.get(stock_url, params=stock_parameters)
AV_response.raise_for_status()
stock_info = AV_response.json()

yesterday_price = float(stock_info["Time Series (Daily)"][f"{YESTERDAY}"]["4. close"])
day_before_yesterday_price = float(stock_info["Time Series (Daily)"][f"{DAY_BEFORE_YESTERDAY}"]["4. close"])
percent_difference = round((yesterday_price - day_before_yesterday_price) / yesterday_price * 100, 2)

if percent_difference > 0:
    symbol = "🔺"
elif percent_difference < 0:
    symbol = "🔻"

if percent_difference >= 5 or percent_difference <= -5:

    # Get the first 3 news pieces for the COMPANY_NAME

    news_url = "https://newsapi.org/v2/everything?"
    news_parameters = {"q": COMPANY_NAME,
                       "from": DAY_BEFORE_YESTERDAY,
                       "sortBy": "popularity",
                       "apiKey": NEWS_APIKEY
                       }

    news_response = requests.get(url=news_url, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]

    news_text = ""

    for item in news_data[:3]:
        text = f"Headline: {item["title"]}\nBrief: {item["description"]}\n\n"
        news_text += text

    # Send a message with the percentage change and each article's title and description to your whatsapp.

    client = Client(TWILIO_account_sid, TWILIO_auth_token)
    message = client.messages.create(
        body=f"{STOCK}: {abs(percent_difference)} {symbol}\n\n{news_text}",
        from_="whatsapp:+1XXXXXXXXXX",
        to="whatsapp:+1XXXXXXXXXX",
    )
    print(message.status)
