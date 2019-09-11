# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:46:10 2019

@author: ANWESHA
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

plt.title('Gaussian distribution')
plt.legend()
plt.show()
