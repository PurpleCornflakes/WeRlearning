import numpy as np 
import matplotlib.pyplot as plt 
'''
logistic model: x(n+1)-x(n)= (a-1)*x(n)-a*x(n)^2
RHS : birth and death of the species.
'''
# a in [0,4], x0 in [0,1]
# when n -> infinity, x_n could be
'''
1. steady
2. periodic
3. chaotic
'''

# def logistic(x0, a, n):
# 	if n==0:
# 		return x0
# 	return a*logistic(x0, a, n-1)*(1.-logistic(x0, a, n-1))

def next_x(a,x0):
	x=x0;
	while True:
		yield x
		x=a*x*(1-x)
# print logistic(0.5, 0.5, 1)

iter_n=20
def x_t(a,ax):
	xx = [0]*iter_n
	for i in range(iter_n):
		xx[i] = logistic(0.3, a, i)
	ax.plot(range(iter_n),xx,'-')
	ax.set_title("$a=%.2f$"%(a,)) 

f,axes=plt.subplots(2,3)

x_t(0.5, axes[0][0])
x_t(2.0, axes[0][1])
x_t(3.2, axes[0][2])
x_t(3.5, axes[1][0])
x_t(3.55, axes[1][1])
x_t(3.7, axes[1][2])
plt.show()