# To test Expectation Maximization Algorithm
# It works very well when estimate pA, pB

import numpy as np 
from scipy.stats import binom

# Generate k groups of [H, T, H, H, T...], each of size n
pA = 0.9
pB = 0.5

n = 10
k = 500

# choose a coin
pp = np.random.choice([pA,pB], k)
# m is like the usual observable random variable X
mm = np.random.binomial(n, pp, k) 

# p(m|Z)
def R(m, n, theta):
	return binom.pmf(m, n, theta)

# p(Z|m), Z {0: coin A, 1: coin B} is the hidden variable, 
def Pz(m, z, thetas):
	return R(m, n, thetas[z])/np.sum([R(m, n, theta) for theta in thetas])

# Dynamic programming to maximize expectation over each Z
# For this simple case we use analytical results directly
def thetas_iter(thetas):
	return [np.sum([m * Pz(m, z, thetas) for m in mm]) \
		/np.sum([n * Pz(m, z, thetas) for m in mm]) \
		for z in [0,1]]

# initial parameters shall not be the same
thetas = [0.8, 0.6]
tmax = 100
for t in range(tmax):
	thetas = thetas_iter(thetas)
	print("res = {0:.3f}, {1:.3f}, err = {2:.4f}, {3:.4f}".format(thetas[0],thetas[1],abs(thetas[0]-pA)/pA, abs(thetas[1]-pB)/pB))

