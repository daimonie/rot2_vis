import numpy as np


class Face:
	_points = -1;
	def __init__(self, point1, point2, point3, point4):
		self._points = np.array([point1, point2, point3, point4]); 
		
	def rotate(self, rotation_matrix):
		for i in range(0,4):
			row = self._points[i] 
			
			col = row.T
			col = np.dot(rotation_matrix, col)
			row = col.T   
			
			for j in range(0,3):
				self._points[i,j] = row[j] 
	def plotdata(self):
		data_x = self._points[:,0]
		data_y = self._points[:,1]
		data_z = self._points[:,2]
		 
		x,y,z = data_x, data_y, data_z
		
		
		return x,y,z
	def translate(self, x, y, z):
		for i in range(0,4):
			self._points[i, 0] += x;
			self._points[i, 1] += y;
			self._points[i, 2] += z;