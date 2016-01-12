
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from face import *
from cube import *
from dtwod import *
from monty import *
fig = plt.figure()
ax = fig.gca(projection='3d')
#Incredible rotation matrix

monty = Monty()
collection = [[],[],[],[]]
for xx in range(0,4):
    collection[xx] = []
    for yy in range(0,4):
        collection[xx].append( Dtwod() )
        
        collection[xx][yy].rotate( monty.get_field_r(xx,yy))
        
for xx in range(0,4): 
    for yy in range(0,4):
        collection[xx][yy].translate(5*xx-10, 5*yy-10, 0); 
 
def animate(frame):
	global fig, ax, collection, jacti
        ax.clear ()
        
        frame += 1 
        frame_max = 1
        
        monty.perturb();
            
	for xx in range(0,4):
            for yy in range(0,4): 
                if monty.is_animated(xx,yy):
                    collection[xx][yy].rotate( monty.get_field_r(xx,yy)) 
                
                plot_data = collection[xx][yy].plotData(opacity=0.95, evencolour='k', oddcolour='y') 
                
                for i in range(0,len(plot_data)):
                        ax.add_collection3d(plot_data[i])
                        
	plt.title( "Frame %d" % frame)
                 
	return frame

block_lim = 10;
ax.set_xlim(-block_lim, block_lim) 
ax.set_ylim(-block_lim, block_lim) 
ax.set_zlim(-block_lim, block_lim)  
ax.view_init(90, 180)   
ani = animation.FuncAnimation(fig, animate, interval=1)

plt.show()