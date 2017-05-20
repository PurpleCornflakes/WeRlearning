from distributions_plot import Poisson_distribution
import numpy as np
import matplotlib.pyplot as plt

p = 0.2 
sim_N = 100000

t = 100.
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

ax1.hist(kk, bins=range(100), normed=True, label="histo")
Poisson_distribution(p*t, range(100), ax1, ax2)
ax1.legend()
plt.show()



