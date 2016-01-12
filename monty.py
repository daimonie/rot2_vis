import numpy as np
import copy as cp
class Monty:
    beta        = None
    j_one       = None
    j_two       = None
    j_three     = None
    
    field_s     = None
    field_r     = None
    field_u     = None
    has_changed =  None
    bath_u      =  None
    
    site_energy = None
    
    def __init__(self, **kwargs):
        print "Welcome to Monty, a 4x4 simulation of the lattice D2D model";
        
        #Recall that the constructor needs to set each member variable, otherwise weird stuff happens
        ising = lambda s: 2.0 * (s>0.5) - 1.0;
        
        self.field_s = ising(np.random.rand(4,4))
        self.site_energy = np.zeros((4,4))
        self.field_r = np.zeros( (4,4,3,3) )
        self.field_u = np.zeros( (2, 4,4,3,3) ) 
        self.has_changed = np.zeros((4,4)); 
        self.bath_u = np.zeros( (8,3,3) );
        
        self.beta = kwargs.get('temperature', 0.5);
        self.j_one = kwargs.get('jone', 0.5);
        self.j_two = kwargs.get('jtwo', 0.5);
        self.j_three = kwargs.get('jthree', 1.0);
        
        #Initialise u bath_u
        self.bath_u = np.zeros( (8,3,3) ); #This works just fine. Why didn't I use it before?
        
        
        self.bath_u[0][0][0] = 1; 
        self.bath_u[0][1][1] = 1; 
        self.bath_u[0][2][2] = 1; 
         
        self.bath_u[1][0][0] = -1; 
        self.bath_u[1][1][1] = -1; 
        self.bath_u[1][2][2] = 1;
         
        self.bath_u[2][0][1] = 1; 
        self.bath_u[2][1][0] = -1; 
        self.bath_u[2][2][2] = -1;
         
        self.bath_u[3][0][1] = -1; 
        self.bath_u[3][1][0] = 1; 
        self.bath_u[3][2][2] = -1;              
         
        self.bath_u[4][0][0] = -1; 
        self.bath_u[4][1][1] = 1; 
        self.bath_u[4][2][2] = -1;                      
         
        self.bath_u[5][0][0] = 1; 
        self.bath_u[5][1][1] = -1; 
        self.bath_u[5][2][2] = -1;      
         
        self.bath_u[6][0][1]= -1; 
        self.bath_u[6][1][0] = -1; 
        self.bath_u[6][2][2] = 1;                       
 
        self.bath_u[7][0][1] = 1; 
        self.bath_u[7][1][0] = 1; 
        self.bath_u[7][2][2] = 1;   
        
        #Initialise randomly, full chaos
	for xx in range(0,4): 
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
                
                self.field_r[xx][yy] = cp.deepcopy(rot)
                
                alea = np.random.randint(0, high=7, size=3);
                
                self.field_u[0][xx][yy] = cp.deepcopy( self.bath_u[alea[0]] )
                self.field_u[1][xx][yy] = cp.deepcopy( self.bath_u[alea[1]] ) 
                
                self.site_energy[xx][yy] = self.forward_energy( xx, yy, rot, self.field_u[0][xx][yy], self.field_u[1][xx][yy], self.field_s[xx][yy]);
                

        #Get to temperature 
                    
        self.thermalise();
        
    def thermalise(self):
        for i in range(0,5000):
            self.perturb()
        
    def is_animated(self, xx, yy):
        return self.has_changed[xx][yy]
        
    def get_jactus(self, xx, yy):
        return 0
    def get_field_r(self, xx, yy):
        return self.field_r[xx][yy];
    def random_matrix(self):
        
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
        
        return rot
    def perturb(self):
        alea = np.random.randint(0, high=3, size=3);
         
        self.has_changed = np.zeros((4,4))
        #self.has_changed[random_site[0]][random_site[1]] = 1;
            
        if alea[2] == 0:
            self.flip_r(alea[0], alea[1])
        elif alea[2] == 1:
            self.flip_ux(alea[0], alea[1])
        elif alea[2] == 2:
            self.flip_uy(alea[0], alea[1])
        elif alea[2] == 3:
            self.flip_uz(alea[0], alea[1])
        
        #self.field_r[random_site[0]][random_site[1]] = np.dot( rot, np.linalg.inv(self.field_r[random_site[0]][random_site[1]])); 
    
    def flip_r( self, xx, yy ):
        
        random_rotation = self.random_matrix()
        ising = np.random.rand()
        
        forward_energy = self.forward_energy( xx, yy, random_rotation, self.field_u[0][xx][yy], self.field_u[1][xx][yy], ising);
        
        energy_difference = self.site_energy[xx][yy] - forward_energy
        
        accept = False
        
        if energy_difference < 0:
            accept = True;
        else:
            if np.exp(-self.beta * energy_difference ) > np.random.rand():
                accept = True;
        
        if accept == True:
            self.field_s[xx][yy] = ising
            self.field_r[xx][yy] = random_rotation
            self.has_changed[xx][yy] = 1
            print "Site (%d, %d) rotates" % (xx,yy)
        
    def flip_ux( self, xx, yy ):
        return
    def flip_uy( self, xx, yy ):
        return
    def flip_uz( self, xx, yy ):
        return
    def forward_energy(self, xx, yy, r, ux, uy, s):
        energy = 0.0
        
        x_next = xx + 1;
        x_prev = xx - 1;
        
        y_next = yy + 1;
        y_prev = yy - 1;
        
        if x_next > 3:
            x_next -= 4;
        if x_prev < 0:
            x_prev += 4;
            
        if y_next > 3:
            y_next -= 4;
        if y_prev < 0:
            y_prev += 4; 
        
        results = np.zeros((4,3,3));
        
        results[0] = np.dot( self.field_s[xx][y_prev] * (s * np.dot( uy, r) ), self.field_r[xx][y_prev]) 
        results[3] = np.dot( self.field_s[x_prev][yy] * (s * np.dot( uy, r) ), self.field_r[x_prev][yy]) 
        
        
        results[1] = np.dot(s * np.dot(self.field_u[0][x_next][yy], self.field_r[x_next][yy]), r)  
        results[2] = np.dot(s * np.dot(self.field_u[1][xx][y_next], self.field_r[xx][y_next]), r)  
        
        for result in results:
            energy += self.j_one * result[0][0]; 
            energy += self.j_two * result[1][1]; 
            energy += self.j_three * result[2][2]; 
        return energy