import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ.get('STOCK_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
account_sid = 'ACb3a857027b035b82a0af8215050f29c6'
auth_token = os.environ.get('AUTH_TOKEN')
symbol = ''


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

data2 = data["Time Series (Daily)"]
data_list = [value for (key, value) in data2.items()]

stock_value_day1 = float(data_list[0]["4. close"])
stock_value_day2 = float(data_list[1]["4. close"])
diff = abs(stock_value_day2-stock_value_day1)
if diff < 0:
    symbol = "up"
else:
    symbol = "down"
print(diff)
percent_diff = stock_value_day1/20
print(percent_diff)
# change to test code, should be diff > percent_diff
if diff*3 > percent_diff:
     print("Get News")
else:
    print("No news")


news_parameters = {
    "apiKey": "26b636b79b784af7af200e5f148dd19d",
    "q": COMPANY_NAME,
}
response2 = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
response2.raise_for_status()
data_news = response2.json()
articles = data_news["articles"]
three_articles = articles[:3]
print(three_articles)

messages = [f"{STOCK}: {symbol} \nHeadline: {article["title"]}. \nBrief: {article['description']}" for article in three_articles]
client = Client(account_sid, auth_token)
for msg in messages:
    message = client.messages \
        .create(
            body=msg,
            from_=os.environ.get('NUMBER1'),
            to=os.environ.get('NUMBER0'),
        )


