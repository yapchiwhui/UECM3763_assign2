# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#task 1-1 : simulating geometric brownian motion
import pylab as p
import numpy as np
#setup parameters
mu = 0.1;
sigma = 0.26; 
S0 = 39;
n_path = 5; 
n = n_partitions = 1000;

#calculate expected value of s3,t=3
E = S0 * p.exp (mu*3)
msg = 'The expected value of S(3) is %.13f' %E
print (msg)

#calculate value for variance S3, t=3
Var = S0**2 * (p.exp(2*mu*3)) * (p.exp(sigma*sigma*3)-1)
msg = 'The variance of S3 is %.13f' %Var
print(msg)

#stimulate 1000 runs of GBM for 0<t<3
#creat brownian path
t = p.linspace(0,3,n+1);
dB = p.randn(n_path, n+1) / p.sqrt(n/3); 
dB[:,0] = 0; #set the first column as zero
B = dB.cumsum(axis=1); #sum over each row for eery olumn

#calculate stock price at time t 
nu = mu - sigma*sigma/2.0;
S = p.zeros_like(B); 
S[:,0] = S0 #the first column is S0=39
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:]);

#plot 5 realization of GBM
S = S[0:5] #choose only first 5 rows to plot

#add some description to the axis and title
p.title('Geometric Brownian Motion');
p.xlabel('t');
p.ylabel('stock price t time t, X(t)');

#plot the grph and show it
p.plot(t,S.transpose());
p.show();

#calculate expectation value of s3, E[s(3)]
S3 = S[:,-1] #price of time 3 for each row
E_S3= np.mean(S3); #find expected price by finding the mean
msg = 'The expected value of S(3) is %.13f' %E
print (msg)

#calculate value for variance S3, Var[S(3)]
Var_S3 = np.var(S3)
msg = 'The variance of S3 is %.13f' %Var_S3
print(msg)

#calculate P[S(3)>39]
count = 0; 
total=0;
for i in range(5):
    if S3[i]>39:
        count = count +1
        total = total +S3[i]
P = count / n_path
msg = 'P[S(3)>39] is %.13f' %P
print (msg)

#calculate E[S(3)|S(3)>39]
conditional_P = total / count
msg = 'E[S(3)|S(3)>39] is %.13f' %conditional_P
print(msg)

