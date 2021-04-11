from pandas_datareader import data as pdr
import datetime
import calendar 
import os.path
import sys
import yfinance as yf
yf.pdr_override()
import pandas as pd
pd.set_option('display.max_rows', None)

if len(sys.argv) < 2:
	stockname = "INTC"
else:
	stockname = sys.argv[1]
	
try:

	print(stockname)
	filename = "data/" + stockname + "/" + stockname + "_1wk.csv"
	dirname = "data/" + stockname 
			
	if os.path.exists(dirname) == False :
		os.mkdir(dirname)
				
	if '/' not in stockname and  '^' not in stockname and  '-' not in stockname :
		print("start to download for " + stockname + " per week")			
		thesymbol = yf.Ticker(stockname)
		hist = thesymbol.history(period="max",interval="1wk",prepost="True",actions="True")
		hist.to_csv(filename)

except IndexError:	
	print("IndexError:")






