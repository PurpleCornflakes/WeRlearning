#This plt is to test the fact that 
# if X ~ Gaussian(0,1), X_1**2+X_2**2 ~ EXP(1/2)

import numpy as np 
import matplotlib.pyplot as plt 

x1=np.random.randn(10000)
x2=np.random.randn(10000)
xx=np.random.exponential(2,10000)
y=x1**2+x2**2
# plt.hist(x)
f,(ax1,ax2)=plt.subplots(1,2)
ax1.hist(y,bins=100,normed=True)

ax1.set_xlim([0,20])

ax2.hist(xx,bins=100,normed=True)
ax2.set_xlim([0,20])

plt.show()