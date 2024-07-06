import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from config import stock_ticker
import pandas as pd
import matplotlib.pyplot as plt

stock_data = pd.read_csv(f'data/{stock_ticker}_last_year.csv', index_col=0, parse_dates=True)

plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.title(f'{stock_ticker} Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()