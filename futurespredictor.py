import requests
import pandas_datareader
import datetime
import pandas
import numpy as np
import matplotlib.pyplot as plt
import scipy
import math
from sklearn.linear_model import LinearRegression

url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=EUR&to_symbol=USD&apikey=#APIKEY'
r = requests.get(url)
data = r.json()
closes = pandas.DataFrame(data.close[:(data.index(data.key('2024-02-09')))], index=pandas.date_range("02092024", periods=81),
                            columns=['Weekly Closing Price'])


cy = (pandas_datareader.DataReader('DGS1MO', 'fred', datetime.date.today())) / 100

date = "03032025" #hypothetical

neartermpr = closes.iloc[[date]]
rr = (neartermpr - closes[-1]) / neartermpr
pr = (closes[-1] - neartermpr) / neartermpr

def trcalc():  
    tr = pr + rr + cy
    
plt.scatter(closes.index, closes.values)
closevals = np.array(closes.values)
lowest = np.min(closevals)
highest = np.max(closevals)
range = highest - lowest
percentile = range / 100

bestpercentdeterminer = []

for k in range(0, 100):
    higherthan = []
    others = []
    for i in closevals:
        if i > lowest:
            higherthan.append(i)
        else:
            others.append(i)
    mean1 = np.mean(np.array(higherthan))
    mean2 = np.mean(np.array(others))
    stdev1 = np.std(np.array(higherthan))
    stdev2 = np.std(np.array(others))
    zs1 = [((u - mean1) / stdev1) for u in higherthan]
    zs2 = [((u - mean1) / stdev1) for u in others]
    zmean1 = np.mean(np.array(zs1))
    zmean2 = np.mean(np.array(others))
    pval1 = scipy.stats.norm.sf(abs(zmean1))
    pval2 = scipy.stats.norm.sf(abs(zmean2))
    bestpercentdeterminer.append(math.log(pval1) + math.log(pval2))
    lowest += percentile

prel = bestpercentdeterminer.index(bestpercentdeterminer.max())
higherprob = (closevals.count(t > closevals[prel] for t in closevals)) / len(closevals)
contango = False
if higherprob >= 0.5:
    contango is True

if contango is False and pr > 0:
    trcalc()
else:
    closeindex = list(range(0, len(closevals)))
    bx = np.sum(np.array( [(u - np.mean(np.array(closeindex)) ** 2) for u in closeindex]))
    by = np.sum(np.array( [(u - np.mean(np.array(closes.values)) ** 2) for u in closes.values]))
    bxy = np.sum(np.array([(u - np.mean(np.array(closeindex)) for u in closeindex) * (t - np.mean(np.array(closes.values)) for t in closes.values)]))
    b2 = bxy / bx
    b1 = np.mean(np.array(closes.values)) - (b2 * np.mean(np.array(closeindex)))
    nextvalpredict = b1 + (b2 * (math.log(closeindex[-1] + 1))) + math.e
    trcalc()
