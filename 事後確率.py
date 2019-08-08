# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 17:41:09 2019

@author: ShimaLab
"""

import numpy as np
import matplotlib.pyplot as plt


theta_list = [0.8,0.6,0.3]
pi_list = [0.1,0.4,0.5]


n = 10
rr = np.array(list(range(0,11)))
theta = np.array(theta_list)
pi = np.array(pi_list)

post_prob = np.zeros((3,11))

for r in rr: 
    
    sum = 0
    prob = np.zeros(3)
    
    for i in range(0,3):
        
        prob[i] = pi[i]*pow(theta[i],r)*pow((1-theta[i]),n-r)
        sum += prob[i]
    
    #確率計算終了
    
    for i in range(0,3):
         
        post_prob[i][r] = prob[i]/sum
    


plt.plot(rr,post_prob[0],label='$\omega_{1}$')
plt.plot(rr,post_prob[1],label='$\omega_{2}$')
plt.plot(rr,post_prob[2],label='$\omega_{3}$')

plt.xlabel("the number of head times")
plt.ylabel("posteriori probability $P(\omega_{i}|x^{(10)})$")    
plt.legend()
