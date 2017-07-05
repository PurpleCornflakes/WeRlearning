import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

w=5
fig,ax=plt.subplots(ncols=1)
ax.set_xlim([-1.2,1.2])
ax.set_ylim([-1.5,1.5])
line,=ax.plot([],[],"-",color="k",linewidth=1)
dot,= ax.plot([],[],"o",color="red",markersize=20)

def init():
	line.set_data([],[])
	dot.set_data([],[])

def update(t):
	while(t>0):
		x=np.sin(w*t)
		xx=np.linspace(0, x,100)
		yy=0.1*np.sin(10*np.pi*xx/x)
		line.set_data(xx,yy)
		dot.set_data(x,0)
		return (line,dot)


anim=animation.FuncAnimation(fig, update, np.linspace(0,10,1000), init_func=init ,interval=100, repeat=True)
plt.show()