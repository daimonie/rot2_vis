
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

lin_x = np.linspace(-1, 1, 100);
lin_y = np.linspace(-1, 1, 100);
mesh_x, mesh_y = np.meshgrid( lin_x, lin_y );
mesh_z = mesh_x * mesh_y * 0 - 2;
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='g', edgecolors='g', shade=False)


lin_x = np.linspace(-1, 1, 100);
lin_y = np.linspace(-1, 1, 100);
mesh_x, mesh_y = np.meshgrid( lin_x, lin_y );
mesh_z = mesh_x * mesh_y * 0 + 2;
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z,  color='g', edgecolors='g', shade=False)

#########################################################################################
lin_x = np.linspace(-1, 0, 100);
lin_z = np.linspace(0, 2, 100);
mesh_x, mesh_z = np.meshgrid( lin_x, lin_z );
mesh_y = mesh_x * mesh_z * 0 - 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z,  color='k', edgecolors='k', shade=False)

lin_x = np.linspace(-1, 0, 100);
lin_z = np.linspace(0, 2, 100);
mesh_x, mesh_z = np.meshgrid( lin_x, lin_z );
mesh_y = mesh_x * mesh_z * 0 + 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z,  color='k', edgecolors='k', shade=False)

lin_x = np.linspace(0, 1, 100);
lin_z = np.linspace(-2, 0, 100);
mesh_x, mesh_z = np.meshgrid( lin_x, lin_z );
mesh_y = mesh_x * mesh_z * 0 - 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='w', edgecolors='w', shade=False)


lin_x = np.linspace(0, 1, 100);
lin_z = np.linspace(-2, 0, 100);
mesh_x, mesh_z = np.meshgrid( lin_x, lin_z );
mesh_y = mesh_x * mesh_z * 0 + 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='w', edgecolors='w', shade=False)


lin_x = np.linspace(0, 1, 100);
lin_z = np.linspace(0, 2, 100);
mesh_x, mesh_z = np.meshgrid( lin_x, lin_z );
mesh_y = mesh_x * mesh_z * 0 + 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='k', edgecolors='k', shade=False)


lin_x = np.linspace(-1, 0, 100);
lin_z = np.linspace(-2, 0, 100);
mesh_x, mesh_z = np.meshgrid( lin_x, lin_z );
mesh_y = mesh_x * mesh_z * 0 + 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='w', edgecolors='w', shade=False)


lin_x = np.linspace(-1, 0, 100);
lin_z = np.linspace(-2, 0, 100);
mesh_x, mesh_z = np.meshgrid( lin_x, lin_z );
mesh_y = mesh_x * mesh_z * 0 - 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='w', edgecolors='w', shade=False)


lin_x = np.linspace(0, 1, 100);
lin_z = np.linspace(0, 2, 100);
mesh_x, mesh_z = np.meshgrid( lin_x, lin_z );
mesh_y = mesh_x * mesh_z * 0 - 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='k', edgecolors='k', shade=False)



#########################################################################################
lin_y = np.linspace(-1, 0, 100);
lin_z = np.linspace(0, 2, 100);
mesh_y, mesh_z = np.meshgrid( lin_y, lin_z );
mesh_x = mesh_y * mesh_z * 0 - 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z,  color='w', edgecolors='w', shade=False)

lin_y = np.linspace(-1, 0, 100);
lin_z = np.linspace(0, 2, 100);
mesh_y, mesh_z = np.meshgrid( lin_y, lin_z );
mesh_x = mesh_y * mesh_z * 0 + 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z,  color='w', edgecolors='w', shade=False)

lin_y = np.linspace(0, 1, 100);
lin_z = np.linspace(-2, 0, 100);
mesh_y, mesh_z = np.meshgrid( lin_y, lin_z );
mesh_x = mesh_y * mesh_z * 0 - 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='k', edgecolors='k', shade=False)


lin_y = np.linspace(0, 1, 100);
lin_z = np.linspace(-2, 0, 100);
mesh_y, mesh_z = np.meshgrid( lin_y, lin_z );
mesh_x = mesh_y * mesh_z * 0 + 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='k', edgecolors='k', shade=False)


lin_y = np.linspace(0, 1, 100);
lin_z = np.linspace(0, 2, 100);
mesh_y, mesh_z = np.meshgrid( lin_y, lin_z );
mesh_x = mesh_y * mesh_z * 0 + 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='w', edgecolors='w', shade=False)


lin_y = np.linspace(-1, 0, 100);
lin_z = np.linspace(-2, 0, 100);
mesh_y, mesh_z = np.meshgrid( lin_y, lin_z );
mesh_x = mesh_y * mesh_z * 0 + 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='k', edgecolors='k', shade=False)


lin_y = np.linspace(-1, 0, 100);
lin_z = np.linspace(-2, 0, 100);
mesh_y, mesh_z = np.meshgrid( lin_y, lin_z );
mesh_x = mesh_y * mesh_z * 0 - 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='k', edgecolors='k', shade=False)


lin_y = np.linspace(0, 1, 100);
lin_z = np.linspace(0, 2, 100);
mesh_y, mesh_z = np.meshgrid( lin_y, lin_z );
mesh_x = mesh_y * mesh_z * 0 - 1; 
surf = ax.plot_surface(mesh_x, mesh_y, mesh_z, color='w', edgecolors='w', shade=False)


ax.set_xlim(-2, 2) 
ax.set_ylim(-2, 2) 
ax.set_zlim(-2, 2) 
plt.show()