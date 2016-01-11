import numpy as np
from face import *
from mpl_toolkits.mplot3d.art3d import Poly3DCollection 

class Dtwod:
	_faces = [];
	_translation = [0., 0., 0.]
	def __init__(self):
		self._faces = []
		self._translation = [0., 0., 0.]
		
		#define face
		x1 = np.array( [0.5, -0.5, -2.0] )
		x2 = np.array( [0.5, 0.5, -2.0] )
		x3 = np.array( [-0.5, 0.5, -2.0] )
		x4 = np.array( [-0.5, -0.5, -2.0] )
		
		x5 = np.array( [0.5, -0.5, 0.0] )
		x6 = np.array( [0.5, 0.5, 0.0] )
		x7 = np.array( [-0.5, 0.5, 0.0] )
		x8 = np.array( [-0.5, -0.5, 0.0] )
		
		
		x9  = np.array( [0.5, -0.5, 2.0] )
		x10 = np.array( [0.5, 0.5, 2.0] )
		x11 = np.array( [-0.5, 0.5, 2.0] )
		x12 = np.array( [-0.5, -0.5, 2.0] )
		
		self._faces.append( Face(x1, x2, x3, x4) )
		self._faces.append( Face(x9, x10, x11, x12) )
		
		self._faces.append( Face(x1, x2, x6, x5) ) 
		self._faces.append( Face(x2, x3, x7, x6) ) 
		self._faces.append( Face(x3, x4, x8, x7) ) 
		self._faces.append( Face(x1, x4, x8, x5) ) 
		
		
		self._faces.append( Face(x5, x6, x10, x9) ) 
		self._faces.append( Face(x6, x7, x11, x10) ) 
		self._faces.append( Face(x7, x8, x12, x11) ) 
		self._faces.append( Face(x5, x8, x12, x9) ) 
		
		
	def rotate(self, rotation_matrix):
		 
		my_location = self._translation[:] 
		
		self.translate( -my_location[0],  -my_location[1],  -my_location[2] ); 
		  
		for i in range(0,len(self._faces)): 			
			self._faces[i].rotate(rotation_matrix)
			  
		self.translate( my_location[0],  my_location[1],  my_location[2] );  
			 
		
	def translate(self, x, y, z):
            
		self._translation[0] += x;
		self._translation[1] += y;
		self._translation[2] += z;
		 
		for i in range(0,len(self._faces)):
			self._faces[i].translate(x,y,z)	
	def location(self):
		print "I am located at (%.3f, %.3f, %.3f)" % ( self._translation[0],  self._translation[1],  self._translation[2])
		
		
	def plotData(self):
		data = []; 
		for i in range(0,len(self._faces)):
			arr_x, arr_y, arr_z = self._faces[i].plotdata() 
			vertices = [zip(arr_x,arr_y,arr_z)]
			
			color = 'g'
			if i == 1 or i == 2 or i == 4 or i == 7 or i == 9:
				color = 'b'
			
			data.append( Poly3DCollection( vertices, alpha=0.8, color=color))
		return data