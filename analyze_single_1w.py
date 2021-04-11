from pandas_datareader import data as pdr
import datetime
import calendar 
import os.path
import sys
import yfinance as yf
yf.pdr_override()
import pandas as pd
pd.set_option('display.max_rows', None)
from matplotlib import pyplot as plt



if len(sys.argv) < 3:
	stockname = "BA"
	weeknumber = 52
	volumebase = 5000000
else:
	stockname = sys.argv[1]
	weeknumber = int(sys.argv[2])
	volumebase = sys.argv[3]


try:

	filename = "data/" + stockname + "/" + stockname + "_1wk.csv"
	dirname = "data/" + stockname 
		
	if os.path.exists(dirname) == True and os.path.exists(filename) == True :
				
		thesymbol = pd.read_csv(filename)
		thesymbol.head()
		thesymbol['Date'] = pd.to_datetime(thesymbol['Date'])
		
		delta = []
		deltaprecentage = []
		highbar = []
		lowbar = []
		volume = []
		
		for row in thesymbol.iterrows():
			print("<" + stockname + "> on " + str(row[1]["Date"]) + " from " + str(row[1]["Open"]) + " to " + str(row[1]["Close"]) + " delta: " + str(row[1]["Close"] - row[1]["Open"]) )
			delta.append(row[1]["Close"] - row[1]["Open"])
			deltaprecentage.append((row[1]["Close"] - row[1]["Open"])/row[1]["Open"])
			highbar.append(0.02)
			lowbar.append(-0.02)
			if float(row[1]["Volume"]) > float(volumebase) :
				volume.append(0.05)
			else:
				volume.append(0)
				
		
		thesymbol['Delta'] = delta
		thesymbol['DeltaP'] = deltaprecentage		
		thesymbol['HighBar'] = highbar
		thesymbol['LowBar'] = lowbar
		thesymbol['Volume'] = volume
		#thesymbol[-52:].set_index('Date')['Delta'].plot();
		thesymbol[-int(weeknumber):].set_index('Date')['DeltaP'].plot();
		thesymbol[-int(weeknumber):].set_index('Date')['HighBar'].plot();
		thesymbol[-int(weeknumber):].set_index('Date')['LowBar'].plot();
		thesymbol[-int(weeknumber):].set_index('Date')['Volume'].plot();
		
		
		plt.show()

except IndexError:	
	print("IndexError:")






