import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from config import stock_ticker
import pandas as pd
import matplotlib.pyplot as plt

stock_data = pd.read_csv(f'data/{stock_ticker}_last_year.csv', index_col=0, parse_dates=True)
stock_dividend = pd.read_csv(f'data/{stock_ticker}_dividends.csv', index_col=0, parse_dates=True)

plt.figure(figsize=(12, 6))
plt.plot(stock_dividend, label='Dividends')
plt.title(f'{stock_ticker} Dividends')
plt.xlabel('Date')
plt.ylabel('Dividends')
plt.legend()
plt.show()