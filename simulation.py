
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from face import *
from cube import *
from dtwod import *
from monty import *
#Command line arguments.
import argparse as argparse  


parser	= argparse.ArgumentParser(prog="Surface Plot",
  description = "Surface plot of data file")   
parser.add_argument('-b', '--beta', help='Beta value.', action='store', type = float, default = 0.57)    
parser.add_argument('-x', '--jone', help='J1=J2 value.', action='store', type = float, default = 0.57)     
parser.add_argument('-z', '--jthree', help='J3 value.', action='store', type = float, default = 0.57)    
parser.add_argument('--nobath', help='Set bath to unity.', action='store', type = str, default = "bath")    
args	= parser.parse_args() 


beta    = args.beta 
j_one    = args.jone  
j_three   = args.jthree 
nobath   = args.nobath 
 
zz = 1;


fig = plt.figure()
ax = fig.gca(projection='3d')
#Incredible rotation matrix

monty = Monty(temperature=beta, jone=j_one, jtwo=j_one, jthree=j_three) 

collection = [[],[],[],[]]
for xx in range(0,4):
    for yy in range(0,4):
        collection[xx].append(Dtwod())
for xx in range(0,4): 
    for yy in range(0,4):
        collection[xx][yy].rotate( monty.get_field_r(xx,yy, zz)) 
        collection[xx][yy].translate(5*xx-10, 5*yy-10, 0); 

if nobath != "bath":
    print "Setting bath to unit matrices."
    monty.no_bath ();

def animate(frame):
	global fig, ax, collection, jacti, energy, energy_squared, zz
        ax.clear ()
        
        frame += 1 
        frame_max = 1
        
        monty.clear()
        monty.thermalise(times=16)   
        
	for xx in range(0,4):
            for yy in range(0,4): 
                if monty.is_changed(xx,yy, zz):
                    collection[xx][yy].rotate( monty.get_field_r(xx,yy, zz))   
                plot_data = collection[xx][yy].plotData(opacity=0.95, evencolour='k', oddcolour='y')                      
                 
                for i in range(0,len(plot_data)):
                        ax.add_collection3d(plot_data[i])
              
	plt.title( "Frame %d, beta=%.3f, j = diag(%.3f, %.3f, %.3f)" % (frame, monty.beta, monty.j_one, monty.j_two, monty.j_three))
        return frame         

block_lim = 10;
ax.set_xlim(-block_lim, block_lim) 
ax.set_ylim(-block_lim, block_lim) 
ax.set_zlim(-block_lim, block_lim)  
ax.view_init(90, 180)   
ani = animation.FuncAnimation(fig, animate, interval=100)

plt.show()