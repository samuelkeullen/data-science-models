import yfinance as yf #we can create an object that will allow us to access functions to extract data
import pandas as pd
import plotly.graph_objs as go
import plotly

apple = yf.Ticker("AAPL")#creating the object and setting Apple as the company that we'll get the financial info
apple_info= apple.info
apple_info_message = "The financial info of apple:\n{}\n".format(apple_info)
print(apple_info_message)

info_country = apple_info['country']
info_country_message = "Country:\n{}\n".format(info_country)
print(info_country_message)

apple_share_price_data = apple.history(period="max")
share_price_message = "Apple Share Price Data:\n{}\n".format(apple_share_price_data)
print(share_price_message)

apple_share_price_data.head()
apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open")

share_price_message = "New Apple Share Price Data:\n{}\n".format(apple_share_price_data)
print(share_price_message)

#apple.dividends.plot()

fig = go.Figure()

fig.add_trace(go.Candlestick(x = apple_share_price_data.index,
open = apple_share_price_data['Open'],
high = apple_share_price_data['High'],
low = apple_share_price_data['Low'],
close = apple_share_price_data['Close'],
name = 'apple_data'
))

fig.update_layout(title = 'Apple share price', yaxis_title = 'Stock price (USD)')

#fig.show()
plotly.offline.plot(fig)