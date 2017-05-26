import numpy as np 
import matplotlib.pyplot as plt
import itertools as it 

# have a look at how 'a' determine the evolution of x.
def first_n(x0 = 0.1, r = 2, n = 60):
	first_n = [x0]
	x = x0
	for i in range(n-1):
		x = r*x*(1-x)
		first_n.append(x)
	return first_n

def draw_6fig():
	fig, axes = plt.subplots(2,3, sharex=True)

	a = iter([2.5, 2.9, 3.2, 3.5, 3.6, 3.7])
	x0 = iter([0.1]*6)
	for i in range(2):
		for j in range(3):
			r = next(a)
			xx0 = next(x0)
			axes[i][j].plot(range(60), first_n(r = r, x0 = xx0), '-o', markersize= 3)
			axes[i][j].set_title("r = {}, x0 = {}".format(r,xx0))



#draw feignbaum 
def next_x(x0 = 0.1, r = 0.9):
	x = x0
	while True:
		yield x
		x = r*x*(1-x)

def extract(x0, r, n, m):
	xx = next_x(x0 = x0, r = r)
	ans = it.islice(xx, n, m)
	return ans

def feignbaum():
	fig2, ax2 = plt.subplots()
	rr = []
	xx = []
	x0 = 0.1
	for r in np.linspace(2.6, 4, 100):
		seq = list(set(extract(x0, r, 100, 200)))
		seqr = [r]*len(seq)
		for i in range(len(seq)):
			xx.append(seq[i])
			rr.append(seqr[i])
	ax2.plot(rr, xx, 'o', markersize=1)

if __name__=="__main__":
	feignbaum()
	draw_6fig()
	plt.show()
	



