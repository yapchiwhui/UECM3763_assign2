# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:35:59 2015

@author: USer
"""

#task 2 Downloading and manipulating Stock data
import numpy as np
import pylab as p
from pandas.io.data import DataReader as DR
from datetime import datetime as dt

#define function for moving average
def movingaverage (values,window):
    weights = np.repeat(1.0,window)/window
    sma = np.convolve(values,weights,'valid')
    return sma
    
#download Sime Darby stock price for 5 years
start = dt(2010,1,1)
end = dt(2015,5,1)
data = DR("4197.KL", 'yahoo', start,end)
Close_Price = data['Close'].values

#calculate 5-days moving average of Nestle
MA = movingaverage (Close_Price,5)

#plot moving acverage graph
num= len(MA)
t = p.linspace (0,num,num);
p.title('5-day moving average for Sime Darby')
p.xlabel('Days')
p.ylabel('Average stock Price, $RM$')
p.plot(t,MA)
p.show()

#calculate the correlation of Nestle with FTSEKLCI
alldata=['^KLSE' , '4197.KL']
c = DR(alldata, 'yahoo' ,start,end) ['Close']
correlation = c.corr()
print('The correlation is :')
print (correlation)
