# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:46:10 2019

@author: NEHA
"""

import numpy as np
import matplotlib as mlab
import matplotlib.pyplot as plt
from scipy import stats

mu = 5      #mean
sigma = 2   #standard deviation
 
nums = np.random.normal(mu,sigma,1000000)   #generating random gaussian numbers using mu and sigma
#print(nums)

num_bins = 400      #number of 'divisions' on histogram
a=[]                # blank list to contain all values of num in range of 10 after executing for loop below


for i in nums:
    if 0<=i<=10:
        a.append(i)
        
plt.hist(a,num_bins, facecolor = 'red', alpha = 1.0, label = 'Gaussian Histogram')  #plots histogram

#pdf = ((1/(2*(np.pi)*(sigma)**2)**0.5)*(np.exp((-(num_bins-mu)**2)/(2*(sigma**2)))))
#plt.plot(15,((1/(2*(np.pi)*(sigma)**2)**0.5)*(np.exp((-(num_bins-mu)**2)/(2*(sigma**2))))) , linewidth=6, color = 'r', label = 'PDF')


plt.title('Gaussian distribution')
plt.legend()
plt.show()
