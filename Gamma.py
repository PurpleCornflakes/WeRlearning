#by Chen & Ling
#05/17/2017
#ax1: there is a bird, the time of its n_th jump ~ Gamma(n,p)
#ax2: there are N_birds, the time of their n_th jump ~ Gamma(n,N_birds*p)
#No wonder the lambda in Gamma(k,lambda) is called scale parameter
import numpy as np
import matplotlib.pyplot as plt

p = 0.2  # the probability of a jump /s
n = 100  
sim_N = 10000


JumpT = [0]*sim_N
for j in range(sim_N):
	jumpTs = [0]*n
	for k in range(n):
		r = np.random.random()
		jumpTs[k] = -np.log(r)/p

	JumpT[j]=sum(jumpTs)

fig, (ax1,ax2) = plt.subplots(ncols = 2)
ax1.hist(JumpT, bins=100, normed=True, label="histo",)



N_bird = 10
tt = [0]*sim_N
for i in range(sim_N):
	k = 0
	t = 0
	while k < n:
		minn = 1000000.
		for j in range(N_bird):
			r = np.random.random()
			tau = -np.log(r)/p
			if tau <= minn:
				minn = tau
		t += minn
		k += 1
	tt[i] = t

ax2.hist(tt, bins=100, normed=True, label="histo")	
plt.show()
print np.mean(tt)
print np.mean(JumpT)







