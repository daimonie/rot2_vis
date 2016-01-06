
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from face import *
from cube import *

fig = plt.figure()
ax = fig.gca(projection='3d')
#Incredible rotation matrix
collection = Cube() 


jacti = np.random.rand(3,1)

def animate(i):
	global fig, ax, collection, jacti
	ax.clear ()
	
	imax = 100.
	if i % imax == 0:
		jacti = np.random.rand(3,1)
	
	u = jacti * (i%imax)/imax
	
	ax.grid(b=False)

	rot = np.zeros((3,3))

	w = np.sqrt(1-u[0]) * np.sin( 2 * np.pi * u[1])
	x = np.sqrt(1-u[0]) * np.cos( 2 * np.pi * u[1])

	y = np.sqrt(u[0]) * np.sin( 2 * np.pi * u[2])
	z = np.sqrt(u[0]) * np.cos( 2 * np.pi * u[2])
	
	rot[0,0] = 1 - 2 * (y*y+z*z)
	rot[0,1] = 2 * (x*y-z*w)
	rot[0,2] = 2 * (x*z+y*w)
	rot[1,0] = 2 * (x*y+z*w)
	rot[1,1] = 1 - 2 * (x*x+z*z)
	rot[1,2] = 2 * (y*z-x*w)
	rot[2,0] = 2 * (x*z-y*w)
	rot[2,1] = 2 * (y*z+x*w)
	rot[2,2] = 1 - 2 * (x*x+y*y)

	collection.rotate(rot)
		
	plot_data = collection.plotData() 
	
	
	for i in range(0,len(plot_data)):
		ax.add_collection3d(plot_data[i])
	
	ax.set_xlim(-2, 2) 
	ax.set_ylim(-2, 2) 
	ax.set_zlim(-2, 2) 
	
	label_title = "Rotated for randoms [%.3f, %.3f, %.3f]" % (u[0], u[1], u[2])
	plt.title( label_title)

ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()