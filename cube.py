import numpy as np
from face import *
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


class Cube:
	_faces = [];
	def __init__(self):
		self._faces = []
		#define face
		x1 = np.array( [0.5, -0.5, -2.0] )
		x2 = np.array( [0.5, 0.5, -2.0] )
		x3 = np.array( [-0.5, 0.5, -2.0] )
		x4 = np.array( [-0.5, -0.5, -2.0] )
		
		x5 = np.array( [0.5, -0.5, 2.0] )
		x6 = np.array( [0.5, 0.5, 2.0] )
		x7 = np.array( [-0.5, 0.5, 2.0] )
		x8 = np.array( [-0.5, -0.5, 2.0] )
		
		self._faces.append( Face(x1, x2, x3, x4) )
		self._faces.append( Face(x5, x6, x7, x8) )
		self._faces.append( Face(x1, x2, x6, x7) )
		self._faces.append( Face(x2, x3, x7, x8) )
		self._faces.append( Face(x4, x3, x7, x8) )
		self._faces.append( Face(x1, x4, x8, x5) )
		
		
	def rotate(self, rotation_matrix):
		for i in range(0,len(self._faces)):
			self._faces[i].rotate(rotation_matrix)
		
	def plotData(self):
		data = []; 
		for i in range(0,len(self._faces)):
			arr_x, arr_y, arr_z = self._faces[i].plotdata() 
			vertices = [zip(arr_x,arr_y,arr_z)]
			
			data.append( Poly3DCollection( vertices, alpha=0.5, color='g'))
		return data