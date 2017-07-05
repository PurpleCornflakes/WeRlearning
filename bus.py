import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.animation as animation

x_begin = 20
x_end = 50
stop_x = [20, 30, 40, 50]
stop_interval = [10, 10, 10, 10]
fig, ax = plt.subplots(ncols=1)
class bus:
	def __init__(self):
		self.x = x_begin
		self.y = 2
		self.speed = 1
		self.timer = 0
		self.arrive = False
		self.t = 0
		self.isforward = True

	def switch(self):
		self.y = 1 if self.y == 2 else 2

	def move(self):
		if self.y == 2:
			self.x += self.speed
		else:
			self.x -= self.speed
		self.t += 1

	def draw(self,axes=ax):
		dot,= ax.plot([],[],"o",color="red",markersize=20)
		ax.set_xlim([10,60])
		ax.set_ylim([0,3])

		def draw_init():
			dot.set_data([],[])
			return dot
		def drive(tt):
			x0 = self.x
			next_x = x0 + self.speed
			if self.t == 0:
				self.move()
				dot.set_data(self.x,self.y)
				return dot
				
			if x0 not in stop_x:
				if next_x in stop_x:
					self.timer = 0
					self.move()
					self.speed = 0
				else:
					self.move()
					self.speed = 1
				dot.set_data(self.x,self.y)
				return dot

			if self.timer == stop_interval[0]:
				if self.x == x_begin or self.x == x_end:
					self.switch()
				self.speed = 1
				self.move()
				dot.set_data(self.x,self.y)
				return dot

			if self.x in stop_x:
				self.timer += 1
				self.t += 1
				dot.set_data(self.x,self.y)
				return dot
		anim = animation.FuncAnimation(fig, drive, range(1000), init_func=draw_init, interval=500)
		plt.show()
		

bus1 = bus()
bus1.draw()
