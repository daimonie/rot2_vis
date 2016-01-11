
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
        
        collection[xx][yy].translate(2*xx-4, 2*yy-4, 0);
        
        collection[xx][yy].location()
 
def animate(frame):
	global fig, ax, collection, jacti
        ax.clear ()
        
        frame += 1 
        frame_max = 1500
	for xx in range(0,4):
            for yy in range(0,4):
                #if monty.is_animated(xx,yy):
                    #jactus = monty.get_jactus(xx,yy);
                plot_data = collection[xx][yy].plotData() 
                
                for i in range(0,len(plot_data)):
                        ax.add_collection3d(plot_data[i])
                 
	return frame

block_lim = 25;
ax.set_xlim(-block_lim, block_lim) 
ax.set_ylim(-block_lim, block_lim) 
ax.set_zlim(-block_lim, block_lim)  
ax.view_init(90, 180)   
ani = animation.FuncAnimation(fig, animate, interval=100)

plt.show()