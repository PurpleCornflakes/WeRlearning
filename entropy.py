import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import *

# entropy = -sum(p_iln(p_i))
def entropy_cal(p_list):
	entropy = 0
	for p in p_list:
		entropy -= p*np.log(p)
	return entropy

n = 100
mu = 0
sigma = 0.5

gd = norm(mu,sigma)
xx = np.linspace(-5, 5, n)
# plt.plot(xx, gd.pdf(xx))
# plt.show()

print("uniform entropy: ",entropy_cal([1.0/n]*n))
print("Gaussian entropy: ",entropy_cal(gd.pdf(xx)/sum(gd.pdf(xx))))
