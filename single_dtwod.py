
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from face import *
from cube import *
from dtwod import *

fig = plt.figure()
ax = fig.gca(projection='3d')
#Incredible rotation matrix

collection = Dtwod() 
collection.translate( 0.0, 0.0, 0.0 );


jacti = np.random.rand(3,1)
 
def animate(frame):
	global fig, ax, collection, jacti
	ax.clear ()
	
	frame += 1 
	frame_max = 500.
	 	
	if frame % frame_max == 0:
		jacti = np.random.rand(3,1)
		print "New set of random numbers!"
	
	u = jacti * (frame%frame_max)/frame_max
	
	
	xfreq = 10 * 2.0 * np.pi / frame_max
	yfreq = xfreq
	zfreq = 2.0 * xfreq
	
	dx = np.cos( xfreq * frame ) * np.cos( zfreq * frame ) - collection._translation[0]
	dy = np.sin( yfreq * frame ) * np.cos( zfreq * frame ) - collection._translation[1]
	dz = np.sin( zfreq * frame ) - collection._translation[2]
	
	collection.translate( dx, dy, dz);
	 
	if collection._translation[2] > 10:
		plt.close()
		raise Exception("Error in translate")
		
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
	 
	label_title = "Plotting [%.1f], z = %.3f" % ( (frame - frame % frame_max)/frame_max, collection._translation[2])
	plt.title( label_title)
	
	return frame

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()