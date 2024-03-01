"""This is day 36 project from Dr angela Yu's course 100 days of python
This is a stock price and news api using twilio api to send stock price
and news to your phone number"""




#-----------------------------#
import os
import time
from datetime import datetime
import requests
import pandas as pd
from twilio.rest import Client
#-----------------------------#
API_STOCKS = 'API key for stocks api'
API_NEWS = 'API key for news api'
STOCK = "TSLA" # - Entity symbol
#-----------------------------#
url_stoks =f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={API_STOCKS}"
news_url = f'https://newsapi.org/v2/everything?q={STOCK}&apiKey={API_NEWS}'
#-----------------------------#
def get_stock_price(url:str)->pd.DataFrame:
    """returns stock data
    Args:
        url (str): F string url containing stock and api key

    Returns:
        pd.DataFrame: stock data ordered by date descending
    """
    response = requests.get(url,timeout=10)
    data = response.json()
    df_original = pd.json_normalize(data['Time Series (Daily)'])
    df = df_original.T
    df = df.reset_index()
    df['date'] = df['index'].apply(lambda x: x.split('.')[0])
    df['metric'] = df['index'].apply(lambda x: ' '.join(
        x.split(' ')[1:]).split('.',maxsplit=1)[0].strip())
    metric_mapping = {
        'open': 'open', 
        'high': 'high', 
        'low': 'low', 
        'close': 'close', 
        'volume': 'volume'
    }
    df['metric'] = df['metric'].map(metric_mapping)
    df_pivot = df.pivot(index='date', columns='metric', values=0)
    df_pivot.reset_index(inplace=True)
    df_pivot['date'] = pd.to_datetime(df_pivot['date'])
    df_pivot = df_pivot.sort_values(by='date',ascending=False)
    df_pivot['high'] = df_pivot['high'].astype(float)
    df_pivot['low'] = df_pivot['low'].astype(float)
    df_pivot['close']= df_pivot['close'].astype(float)
    df_pivot['open'] = df_pivot['open'].astype(float)
    df_pivot['volume'] = df_pivot['volume'].astype(int)
    df_pivot['Diff_Start_end'] = df_pivot['high'] - df_pivot['low']
    df_pivot['Diff_Start_end'] = df_pivot['Diff_Start_end'].astype(float)
    df_pivot['day_change'] = df_pivot['close'] / df_pivot['open']/100
    df_pivot['day_change'] = df_pivot['day_change'].map("{:.2%}".format)
    df_pivot['closing_differences'] = df_pivot['close'].diff()/df_pivot['close']
    df_pivot['closing_differences'] = df_pivot['closing_differences'].map("{:.2%}".format)
    df_pivot.reset_index(inplace=True,drop=True)
    return df_pivot


def get_news_info(url:str)->pd.DataFrame:
    """Gets the news on stock symbol
    Args:
        url (str): Api endpoint for news
    Returns:
        dataframe: gets all available news on the stock symbol ordered by date descending
    """
    r = requests.get(url,timeout=10)
    data = r.json()
    df = pd.json_normalize(data['articles'])
    df = df[['author','title','description','url','publishedAt']]
    df['publishedAt'] = pd.to_datetime(df['publishedAt'])
    df = df.sort_values(by='publishedAt',ascending=False)
    return df


def return_message(df_stocks: pd.DataFrame, df_news: pd.DataFrame) -> dict:
    """Returning message to send via twilio
    Args:
        df_stocks (pd.DataFrame): latest stock info
        df_news (pd.DataFrame): latest news for stock
    """
    df_stocks['day_change'] = df_stocks['day_change'].replace('%', '', regex=True).astype(float)
    today_date = datetime.today().date()
    news_yesterday = df_news[df_news['publishedAt'].dt.date == today_date - pd.Timedelta(days=1)]
    stocks_today = df_stocks[df_stocks['date'].dt.date == today_date]
    news_today = df_news[df_news['publishedAt'].dt.date == today_date]
    message_dict = {}
    news_index = 0
    if not stocks_today.empty and stocks_today['day_change'].max() > 0.02:
        for _, news_row in news_today.iterrows():
            message_dict[news_index] = news_row['title']
            news_index += 1
    elif not news_yesterday.empty:
        for _, news_row in news_yesterday.iterrows():
            message_dict[news_index] = news_row['title']
            news_index += 1
    else:
        message_dict[0] = 'No relevant news today'
    return message_dict


def send_message(message_dict: dict) -> None:
    """Sends message to phone if exists.

    Args:
        message (dict): A dictionary containing the message to send.

    Returns:
        None
    """
    if not message_dict:
        print('No message to send')
    else:
        account_id = os.getenv('Acc_id_twilio')
        auth_token = os.getenv('Auth_token_twilio')
        client = Client(account_id,auth_token)
        for _, message_dict in message_dict.items():
            time.sleep(2)
            msg = client.messages \
                            .create(
                                body=message_dict,
                                from_='your twilio number here',
                                to='your personal nr here'
                            )

            print(msg.status)


if __name__ == '__main__':
    stocks = get_stock_price(url_stoks)
    news = get_news_info(news_url)
    message = return_message(stocks, news)
    send_message(message)
