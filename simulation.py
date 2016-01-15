
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
parser.add_argument('--lattice', help='Lattice size (L1).', action='store', type = int, default = 4)    
args	= parser.parse_args() 


beta    = args.beta 
j_one   = args.jone  
j_three = args.jthree 
nobath  = args.nobath 
lattice = args.lattice 

print "Parameters: %.3f, %.3f, %.3f, %s, %d" % (beta, j_one, j_three, nobath, lattice)
zz = 1;


fig = plt.figure()
ax = fig.gca(projection='3d')
#Incredible rotation matrix

monty = Monty(temperature=beta, jone=j_one, jtwo=j_one, jthree=j_three, lattice_size=lattice) 

monty.thermalise(times=2000)   

collection = []
for xx in range(0, monty.lattice_size):
    collection.append([])
    for yy in range(0,monty.lattice_size):
        collection[xx].append(Dtwod())
for xx in range(0,monty.lattice_size): 
    for yy in range(0,monty.lattice_size):
        collection[xx][yy].rotate( monty.get_field_r(xx,yy, zz)) 
        collection[xx][yy].translate(5*xx-10, 5*yy-10, 0); 

energy = 0.0;
energy_squared = 0.0;
samples = 0;


for i in range(0,50):
        monty.thermalise(times= monty.lattice_size**3 * 100) #length three, tau, samples
        current_energy = monty.energy
        
        samples += 1
        energy += current_energy
        energy_squared += current_energy**2
        
        specific_heat = (energy_squared/samples - (energy/samples)**2) * monty.beta**2 /  monty.lattice_size**3 
                
        print "Progress %d/100, beta=%.3f, energy %.3f, specific heat %.3f" % (i, monty.beta, energy/samples/monty.lattice_size**3 , specific_heat)
        
raise Exception("Currently only want a C_V estimate. Beta/Energy/SpecificHeat\n0.78750000\t0.19532510\t0.61418629")
print "Visualising..."
def animate(frame):
	global fig, ax, collection, jacti, energy, energy_squared, zz, beta, samples
        ax.clear ()
        
        frame += 1 
        frame_max = 1
         
        monty.clear()
        #monty.thermalise(times=2500)    
        monty.thermalise(times= monty.lattice_size**3 * 100) #length three, tau, samples
        current_energy = monty.energy
        
        samples += 1
        energy += current_energy
        energy_squared += current_energy**2
        
        specific_heat = (energy_squared/samples - (energy/samples)**2) * monty.beta**2 /  monty.lattice_size**3  
        
	for xx in range(0,monty.lattice_size):
            for yy in range(0,monty.lattice_size): 
                if monty.is_changed(xx,yy, zz):
                    collection[xx][yy].rotate( monty.get_field_r(xx,yy, zz))   
                plot_data = collection[xx][yy].plotData(opacity=0.95, evencolour='k', oddcolour='y')                      
                 
                
                for i in range(0,len(plot_data)):
                        ax.add_collection3d(plot_data[i])
                
	plt.title( "%.3f, %.3f, %.3f, %d, %.3f, %.3f, %.3f, samples %d, lattice_size %d" % (monty.beta, energy/samples/monty.ground/monty.lattice_size**3, specific_heat, samples, monty.j_one, monty.j_two, monty.j_three, samples, monty.lattice_size))
        return frame         

block_lim = 2.5 * monty.lattice_size;
ax.set_xlim(-block_lim, block_lim) 
ax.set_ylim(-block_lim, block_lim) 
ax.set_zlim(-block_lim, block_lim)  
ax.view_init(90, 180)   
ani = animation.FuncAnimation(fig, animate, interval=100)

plt.show()