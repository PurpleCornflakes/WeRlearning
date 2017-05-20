#The plots are to help understand basic distributinons in random phenomena.
import numpy as np 
import math
import matplotlib.pyplot as plt
import scipy.special as sps

def Gaussian_distribution(mu,sigma,ax1,ax2):
	'''
	mu is mean, sigma is standard deviation

	'''
	x = np.linspace(-5,5,1000)
	normalize_factor = 1.0/np.sqrt(2*np.pi*sigma**2)
	y = normalize_factor*np.exp(-(x-mu)**2/2*sigma**2)
	ax1.plot(x,y,'-',color='cornflowerblue')
	ax1.tick_params(labelsize=8)
	ax1.set_xlabel("$x$")
	ax1.set_ylabel("$P(x)$")
	ax1.legend("Gaussian",loc="upper right", fontsize=5)
	ax1.set_title("$e^{(x-\mu)^2/\sigma ^2}:\mu=%d,\sigma=%d$"%(mu,sigma),fontsize=12)

	ax2.plot(x,y,'-',color='cornflowerblue')
	ax2.set_xscale('log')
	ax2.set_yscale('log')
	ax2.tick_params(labelsize=8)


def Poisson_distribution(lambd,extent,ax1,ax2):
	'''
	lambd is N*p*(1-p)

	'''

	y = lambda x: np.exp(-lambd)*lambd**x/math.factorial(x)
	for x in extent:
		ax1.plot(x,y(x),'*',color='y')
		ax1.tick_params(labelsize=8)
		ax1.set_title("$e^{-\lambda}\lambda^k/k!:\lambda=%f$"%(lambd),fontsize=12)
		ax1.set_xlabel("$k$")
		ax1.set_ylabel("$P(k)$")
	for x in range(1,20):
		ax2.plot(x,y(x),'*',color='yellow')
		ax2.tick_params(labelsize=8)
		ax2.set_xscale('log')
		ax2.set_yscale('log')
		ax2.tick_params(labelsize=8)

def Power_Law(alpha,ax1,ax2):
	'''
	alpha is the power 

	'''
	y = lambda x: x**(alpha)
	for x in range(1,100):
		ax1.plot(x,y(x),'o',color='red')
		ax1.tick_params(labelsize=8)
		ax1.set_title("$k^{-a}:a=%s$"%(alpha))
		ax1.set_xlabel("$k$")
		ax1.set_ylabel("$P(k)$")

	for x in range(1,100):
		ax2.plot(x,y(x),'o',color='red')
		ax2.set_xscale('log')
		ax2.set_yscale('log')
		ax2.tick_params(labelsize=8)

def gamma(shape,scale,ax):
	s = np.random.gamma(shape, scale, 10000)
	count, bins, ignored = ax.hist(s, 50, normed=True, histtype='step')

	y = bins**(shape-1)*(np.exp(-bins/scale) /(sps.gamma(shape)*scale**shape))
	ax.plot(bins, y,'-', linewidth=2,label="$k=%.1f,\lambda=%.1f$"%(shape,1/scale))
	ax.tick_params(labelsize=8)
	ax.legend(loc="upper right")
	ax.set_xlabel("$t$")
	ax.set_ylabel("$P(t)$")


def Gamma_distribution():
	'''
	shape is k, the arrival times,scale is theta, 1/lambda
	
	it's Chi-Square (the sum of square of X_i ~ normal distribution) 
	when shape=n/2, lambda=1/2

	it's exponential distribution when shape=1
	'''
	gamma(shape=2.,scale=3.,ax=axes[2][0])
	gamma(shape=2.,scale=2.,ax=axes[2][0])
	gamma(shape=2.,scale=1.,ax=axes[2][0])
	gamma(shape=3.,scale=2.,ax=axes[2][1])
	gamma(shape=2.,scale=2.,ax=axes[2][1])
	gamma(shape=1.,scale=2.,ax=axes[2][1])
	gamma(shape=1.,scale=2.,ax=axes[2][2])
	




f,axes = plt.subplots(3,3, figsize=[15,10])

Gaussian_distribution(mu=0,sigma=1,ax1=axes[0][0],ax2=axes[1][0])
Poisson_distribution(lambd=2,extent=range(1,20),ax1=axes[0][1],ax2=axes[1][1])
Power_Law(alpha=-0.5,ax1=axes[0][2],ax2=axes[1][2])
Gamma_distribution()
# plt.savefig("/Users/qinglingzhang/Desktop/distributions.png",format="png",dpi=100)
plt.show()