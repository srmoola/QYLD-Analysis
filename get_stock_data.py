import os
import yfinance as yf
from datetime import datetime, timedelta
from config import stock_ticker

ticker_symbol = stock_ticker

stock = yf.Ticker(ticker_symbol)

end_date = datetime.now().date()
start_date = end_date - timedelta(days=365)

stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
stock_dividend = stock.dividends
dividends_last_year = stock_dividend[start_date.strftime('%Y-%m-%d'):end_date.strftime('%Y-%m-%d')]

#iterate over the dividends_last_year and print the date and the dividend amount
for date, dividend in dividends_last_year.items():
  #find date for week before and week after the dividend date
  week_before = date - timedelta(days=7)
  week_after = date + timedelta(days=7)
  
  stock_data_week = stock_data[week_before.strftime('%Y-%m-%d'):week_after.strftime('%Y-%m-%d')]
  print(date)
  print(stock_data_week)
  exit()

if not os.path.exists(f'data/{ticker_symbol}'):
  os.makedirs(f'data/{ticker_symbol}')

dividends_last_year.to_csv(f'data/{ticker_symbol}/dividends_past_year.csv')
stock_data.to_csv(f'data/{ticker_symbol}/full_past_year.csv')
