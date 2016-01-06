
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import numpy as np
from face import *

fig = plt.figure()
ax = fig.gca(projection='3d')
#Incredible rotation matrix
def animate(i):
	if i < 1e5:
		ax.cla ()
		
		u = np.random.rand(3,1);

		rot = np.zeros((3,3))

		w = np.sqrt(1-u[0]) * np.sin( 2 * np.pi * u[1]);
		x = np.sqrt(1-u[0]) * np.cos( 2 * np.pi * u[1]);

		y = np.sqrt(u[0]) * np.sin( 2 * np.pi * u[2]);
		z = np.sqrt(u[0]) * np.cos( 2 * np.pi * u[2]);
		
		rot[0,0] = 1 - 2 * (y*y+z*z);
		rot[0,1] = 2 * (x*y-z*w);
		rot[0,2] = 2 * (x*z+y*w);
		rot[1,0] = 2 * (x*y+z*w);
		rot[1,1] = 1 - 2 * (x*x+z*z);
		rot[1,2] = 2 * (y*z-x*w);
		rot[2,0] = 2 * (x*z-y*w);
		rot[2,1] = 2 * (y*z+x*w);
		rot[2,2] = 1 - 2 * (x*x+y*y); 

		#define face
		x1 = np.array([0.,0.,1.]);
		x2 = np.array([1.,0.,1.]);
		x3 = np.array([1.,1.,1.]);
		x4 = np.array([0.,1.,1.]);
		
		single_face = Face(x1, x2, x3, x4); 
		single_face.rotate(rot); 
		arr_x, arr_y, arr_z = single_face.plotdata() 
		
		ax.scatter(arr_x, arr_y, arr_z) 
		
		ax.set_xlim(-2, 2) 
		ax.set_ylim(-2, 2) 
		ax.set_zlim(-2, 2) 

ani = animation.FuncAnimation(fig, animate, interval=2500)
plt.show()