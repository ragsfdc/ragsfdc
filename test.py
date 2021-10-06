from tvDatafeed import TvDatafeed,Interval
import os
import datetime
import logging
import pandas as pd
import numpy as np
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
OHLC_data=TvDatafeed().get_hist(_stock_name,_exchange,Interval.in_daily,n_bars=3000)
print(OHLC_data)
