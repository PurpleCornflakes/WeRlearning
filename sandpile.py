import numpy as np 
import matplotlib.pyplot as plt 


class SandPile(object):
	def __init__(self, N, M, add_pos = "one_side",d_type = "float"):
		self.N = N+2
		self.M = M+2
		self.lattice = np.zeros([self.N,self.M], dtype = d_type)
		self.Xc = 4
		self.i = 0
		self.j = 0
		self.givers_index = None
		self.epsilon = 1

	def cal_num_nonzero(self):
		self.num_nzero = np.sum(np.where(self.lattice[1:-1,1:-1] > 1e-6, 1, 0))/((self.N-2)*(self.M-2))

	def add_sand(self, add_pos, num = 1):
		self.add_pos = add_pos
		if self.add_pos == "one_side":
			ii = np.random.choice(np.arange(self.N-2)+1, size = num)
			jj = np.array([0+1]*num)
		elif self.add_pos == 'center':
			ii = np.array([self.N//2]*num)
			jj = np.array([self.M//2]*num)  
		elif self.add_pos == 'random':
			ii = np.random.choice(np.arange(self.N-2)+1, size = num)
			jj = np.random.choice(np.arange(self.M-2)+1, size = num)
		else:
			raise ValueError("add_pos choices: 'one_side' , 'center', 'random'")
	    
		pos_to_add = np.array(list(zip(ii, jj)))
		for i in range(pos_to_add.shape[0]):
			self.lattice[pos_to_add[i,0],pos_to_add[i,1]] += self.epsilon


	def not_converge(self):
		# '+1' is to convert valid_pos index to lattice index
		self.givers_index = np.argwhere(self.lattice[1:-1,1:-1] > self.Xc) + 1
		if self.givers_index.shape[0] == 0:
			return False
		else:
			return True
		
	def one_relax(self):
		for i in range(self.givers_index.shape[0]):
			self.i = self.givers_index[i,0]
			self.j = self.givers_index[i,1]
			energy = self.lattice[self.i,self.j]
			self.lattice[self.i-1, self.j] += energy/4
			self.lattice[self.i+1, self.j] += energy/4
			self.lattice[self.i, self.j-1] += energy/4
			self.lattice[self.i, self.j+1] += energy/4
			self.lattice[self.i, self.j] = 0

	def plot_lattice(self):
		print(self.lattice.astype(int))

	def run(self, add_pos = "one_side"):
		self.add_sand(add_pos,num=1)
		self.plot_lattice()
		while self.not_converge():
			self.one_relax()
			self.plot_lattice()


np.random.seed(222)
fig, ax = plt.subplots(ncols = 1, nrows = 1)
s = SandPile(5, 5, add_pos = 'one_side')
for i in range(500):
	s.run()



