#by Chen & Ling
#05/17/2017
#ax1: there is a machine, in [0,t] it broke k times ~ Poisson(p*t)
#ax2: there are N macheines, in [0,t] they broke k times ~ Poisson(N*p*t)
#the lambda in Poisson(lambda) is the average arrival times in [0,t]

# from distributions_plot import Poisson_distribution
import numpy as np
import matplotlib.pyplot as plt
import scipy

p = 0.2 
t = 1.
sim_N = 100000

kk = [0]*sim_N

for i in range(sim_N):
	k = 0
	tau = 0
	while tau <= t:
		r = np.random.random()
		tau += -np.log(r)/p
		k += 1
	kk[i] = k


fig, (ax1,ax2) = plt.subplots(ncols = 2)

ax1.hist(kk, bins=range(1,10), normed=True, label="histo")
# Poisson_distribution(p*t, range(10), ax1, ax2)
# ax1.legend()

N = 10
for i in range(sim_N):
	machines = np.zeros(N,dtype=int)
	broken_times = np.zeros(N)
	for j in range(N):
		r = np.random.random()
		tau = -np.log(r)/p
		broken_times[j] = tau
	for m in range(len(machines)):
		if broken_times[m] <= t:
			machines[m] = 1
	kk[i] = sum(machines)



counts,bins,ignored = ax2.hist(kk, bins=10, normed=True)
# Poisson_distribution(p*t*N, range(4), ax1, ax2)

plt.show()



