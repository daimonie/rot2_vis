import numpy as np
class Monty:
    beta = 0.5;
    j_one = 0.5;
    j_two = 0.5;
    j_three = 1.0;
    
    field_s = np.zeros((4,4))
    field_r = []
    field_u = []
    
    has_changed = np.zeros((4,4));
    def __init__(self):
        print "Welcome to Monty, a 4x4 simulation of the lattice D2D model";
        
        #Initialise randomly, full chaos
	for xx in range(0,4):
            self.field_r.append([])
            for yy in range(0,4):

                u = np.random.rand(3,1)
    
                w = np.sqrt(1-u[0]) * np.sin( 2 * np.pi * u[1])
                x = np.sqrt(1-u[0]) * np.cos( 2 * np.pi * u[1])

                y = np.sqrt(u[0]) * np.sin( 2 * np.pi * u[2])
                z = np.sqrt(u[0]) * np.cos( 2 * np.pi * u[2])
                    
                rot = np.zeros((3,3))
                rot[0,0] = 1 - 2 * (y*y+z*z)
                rot[0,1] = 2 * (x*y-z*w)
                rot[0,2] = 2 * (x*z+y*w)
                rot[1,0] = 2 * (x*y+z*w)
                rot[1,1] = 1 - 2 * (x*x+z*z)
                rot[1,2] = 2 * (y*z-x*w)
                rot[2,0] = 2 * (x*z-y*w)
                rot[2,1] = 2 * (y*z+x*w)
                rot[2,2] = 1 - 2 * (x*x+y*y) 
                
                self.field_r[xx].append( rot ) 
                 
        self.thermalise();
        
    def thermalise(self):
        return 0
        
    def is_animated(self, xx, yy):
        return self.has_changed[xx][yy]
        
    def get_jactus(self, xx, yy):
        return 0
    def get_field_r(self, xx, yy):
        return self.field_r[xx][yy];
    def perturb(self):
        random_site = np.random.randint(0, high=3, size=2);
         
        self.has_changed = np.zeros((4,4))
        self.has_changed[random_site[0]][random_site[1]] = 1;
        
        u = np.random.rand(3,1)

        w = np.sqrt(1-u[0]) * np.sin( 2 * np.pi * u[1])
        x = np.sqrt(1-u[0]) * np.cos( 2 * np.pi * u[1])

        y = np.sqrt(u[0]) * np.sin( 2 * np.pi * u[2])
        z = np.sqrt(u[0]) * np.cos( 2 * np.pi * u[2])
            
        rot = np.zeros((3,3))
        rot[0,0] = 1 - 2 * (y*y+z*z)
        rot[0,1] = 2 * (x*y-z*w)
        rot[0,2] = 2 * (x*z+y*w)
        rot[1,0] = 2 * (x*y+z*w)
        rot[1,1] = 1 - 2 * (x*x+z*z)
        rot[1,2] = 2 * (y*z-x*w)
        rot[2,0] = 2 * (x*z-y*w)
        rot[2,1] = 2 * (y*z+x*w)
        rot[2,2] = 1 - 2 * (x*x+y*y) 
        
        self.field_r[random_site[0]][random_site[1]] = np.dot( rot, np.linalg.inv(self.field_r[random_site[0]][random_site[1]])); 