# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:18:42 2015

@author: USer
"""

#task 1-2 stimulating mean reversal process
import pylab as p

#define parameters
alpha = 1 ; 
theta = 0.064 ; 
sigma = 0.27; 
R0=3 ;
t = 1.0;
n_path = 1000; 
n = n_partitions = 1000; 
dt = t/n; 

#creat browian path
T = p.linspace(0,t,n+1)[:-1];
dB = p.randn (n_path, n+1)* p.sqrt(dt);
dB[:,0] = 0; #for all row,first column is zero
B = dB.cumsum(axis=1);

R = p.zeros_like(B) #creat zero matrix with size B
R[:,0] = R0 #set first column of matrix R as 3
for column in range (n):
    R[:,column+1] = R[:,column] +(theta-R[:,column])*dt + [sigma*R[:,column]]*dB[:,column+1]

#plot 5 realization of mean reversal
r = R[0:5:,:-1]#only select 5 realisation
p.xlabel('t');
p.ylabel('R(t)');
p.title('Mean Reversion Model');
p.plot(T,r.transpose());
p.show();

#calculate expectation value of R(1)
R1 = R[: , -1] #pick all value of R(1)
expected_r1 = R1.sum() / n_path
msg = 'The expected value of R(1) is %.13f' %expected_r1
print(msg)

#calculate P[R(1)>2]
count = 0
for i in range(5):
    if R1[i]>2:
        count = count+1
P = count / n_path
msg = 'P[R(1)>2] is %.13f' %P
print (msg)