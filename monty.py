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
    lattice_size = None
    
    energy = None
    ground = None
    
    def __init__(self, **kwargs):
        self.energy = 0.0
        
        self.lattice_size = kwargs.get('lattice_size', 6);
        
        
        
        #Recall that the constructor needs to set each member variable, otherwise weird stuff happens
        ising = lambda s: 2.0 * (s>0.5) - 1.0;
        
        self.field_s = ising(np.random.rand(self.lattice_size,self.lattice_size,self.lattice_size))
        self.site_energy = np.zeros((self.lattice_size,self.lattice_size,self.lattice_size))
        self.field_r = np.zeros( (self.lattice_size,self.lattice_size,self.lattice_size,3,3) )
        self.field_u = np.zeros( (3,self.lattice_size,self.lattice_size,self.lattice_size,3,3) ) 
        self.has_changed = np.zeros((self.lattice_size,self.lattice_size,self.lattice_size));  
        
        self.j_one = -kwargs.get('jone', 0.5);
        self.j_two = -kwargs.get('jtwo', 0.5);
        self.j_three = -kwargs.get('jthree', 1.0);
        self.beta = kwargs.get('temperature', 0.5);
        
        
        print "Welcome to Monty, a %dx%d simulation of the lattice D2D model, starting at beta = %.3f" % (self.lattice_size,self.lattice_size, self.beta);
        self.ground = self.lattice_size**3 *3*(self.j_one + self.j_two + self.j_three)
        
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
	for xx in range(0,self.lattice_size): 
            for yy in range(0,self.lattice_size):
                for zz in range(0,self.lattice_size): 
                    rot = self.random_matrix()
                    
                    self.field_r[xx][yy][zz] = cp.deepcopy(rot)
                    
                    alea = np.random.randint(0, high=7, size=3)
                    
                    self.field_u[0][xx][yy][zz] = cp.deepcopy( self.bath_u[alea[0]] )
                    self.field_u[1][xx][yy][zz] = cp.deepcopy( self.bath_u[alea[1]] ) 
                    
        #Neighbours need to be initialised
	for xx in range(0,self.lattice_size): 
            for yy in range(0,self.lattice_size):
                for zz in range(0,self.lattice_size): 
                    self.site_energy[xx][yy][zz] = self.forward_energy( xx, yy, zz, rot, self.field_u[0][xx][yy][zz], self.field_u[1][xx][yy][zz], self.field_u[2][xx][yy][zz], self.field_s[xx][yy][zz]);
                    self.energy += self.site_energy[xx][yy][zz]

        #Get to temperature  
        self.thermalise();
    def thermalise(self, **kwargs):
        for i in range(0, kwargs.get('times', 1000)):
            self.perturb()
        
    def is_changed(self, xx, yy, zz):
        return self.has_changed[xx][yy][zz] 
    def get_field_r(self, xx, yy, zz):
        return self.field_r[xx][yy][zz];
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
    def rotation_matrix(self):
        raise Exception("Should not be called")
        u = np.array([0.5, 1.0, 0.0])
        
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
    def clear(self): 
        self.has_changed = np.zeros((self.lattice_size,self.lattice_size,self.lattice_size))
    def perturb(self):
        alea = np.random.randint(0, high=self.lattice_size, size=3); 
            
        alea_flip = np.random.randint(0, high=2,size=1); 
        if alea_flip == 0:
            self.flip_r(alea[0], alea[1], alea[2])
        elif alea_flip == 1:
            self.flip_u(alea[0], alea[1], alea[2],0)
        elif alea_flip == 2:
            self.flip_u(alea[0], alea[1], alea[2],1) 
        elif alea_flip == 3:
            self.flip_u(alea[0], alea[1], alea[2],2) 
        
        #self.field_r[random_site[0]][random_site[1]] = np.dot( rot, np.linalg.inv(self.field_r[random_site[0]][random_site[1]])); 
    
    def flip_r( self, xx, yy,zz ):
        
        random_rotation = self.random_matrix()
        
        make_ising = lambda s: 2.0 * (s>0.5) - 1.0;
        ising = make_ising(np.random.rand())
        
        forward_energy = self.forward_energy( xx, yy, zz, random_rotation, self.field_u[0][xx][yy][zz], self.field_u[1][xx][yy][zz], self.field_u[2][xx][yy][zz], ising);
        
        energy_difference =  forward_energy- self.site_energy[xx][yy][zz]  
        if self.accept(energy_difference):
            self.field_s[xx][yy][zz] = ising
            self.field_r[xx][yy][zz] = random_rotation
            self.has_changed[xx][yy][zz] = 1 
            self.site_energy[xx][yy][zz] = forward_energy
            self.energy += energy_difference
            
        
    def flip_u( self, xx, yy, zz, direction): 
        alea = np.random.randint( 0, high=8, size=1); #from u bath_u
        
        forward_energy = 0.0
        if direction == 0:
            self.forward_energy( xx, yy, zz, self.field_r[xx][yy][zz],  self.bath_u[alea] , self.field_u[1][xx][yy][zz], self.field_u[2][xx][yy][zz], self.field_s[xx][yy][zz]); 
        elif direction == 0:
            self.forward_energy( xx, yy, zz, self.field_r[xx][yy][zz],  self.field_u[0][xx][yy][zz] ,self.bath_u[alea], self.field_u[2][xx][yy][zz], self.field_s[xx][yy][zz]); 
        elif direction == 0:
            self.forward_energy( xx, yy, zz, self.field_r[xx][yy][zz],  self.field_u[0][xx][yy][zz] , self.field_u[1][xx][yy][zz], self.bath_u[alea], self.field_s[xx][yy][zz]); 
        else:
            raise Exception("flip_u says direction is unknown")
        
        energy_difference = forward_energy - self.site_energy[xx][yy][zz]
        
        if self.accept(energy_difference):
            #self.has_changed[xx][yy] = 1 only for field_r
            self.field_u[direction][xx][yy][zz] = cp.deepcopy( self.bath_u[alea] )
            self.site_energy[xx][yy][zz] = forward_energy
            self.energy += energy_difference 
    def accept(self, energy_difference):
        result = True;
        
        if energy_difference > 0: 
            
            result   = False;
            boltzman = np.exp( - self.beta * energy_difference )
            jactus   = np.random.rand()
            
            if boltzman > jactus: 
                    result = True; 
        return result; 
    def forward_energy(self, xx, yy, zz, r, ux, uy, uz, s):
        bond_energy = 0.0
        
        x_next = xx + 1;
        x_prev = xx - 1;
        
        y_next = yy + 1;
        y_prev = yy - 1;
        
        z_next = zz + 1;
        z_prev = zz - 1;
        
        if x_next >= self.lattice_size:
            x_next -= self.lattice_size;
        if x_prev < 0:
            x_prev += self.lattice_size;
            
        if y_next >= self.lattice_size:
            y_next -= self.lattice_size;
        if y_prev < 0:
            y_prev += self.lattice_size; 
            
        if z_next >= self.lattice_size:
            z_next -= self.lattice_size;
        if z_prev < 0:
            z_prev += self.lattice_size; 
         
        results = np.zeros((6,3,3)); 
        
        results[1] = np.dot( self.field_s[x_prev][yy][zz] * (s * np.dot( uy, r) ), self.field_r[x_prev][yy][zz].T) 
        results[0] = np.dot( self.field_s[xx][y_prev][zz] * (s * np.dot( ux, r) ), self.field_r[xx][y_prev][zz].T) 
        results[2] = np.dot( self.field_s[xx][yy][z_prev] * (s * np.dot( uz, r) ), self.field_r[xx][yy][z_prev].T) 
        
        results[3] = np.dot(s * self.field_s[x_next][yy][zz] * np.dot(self.field_u[0][x_next][yy][zz], self.field_r[x_next][yy][zz]), r.T)  
        results[4] = np.dot(s * self.field_s[xx][y_next][zz] *  np.dot(self.field_u[1][xx][y_next][zz], self.field_r[xx][y_next][zz]), r.T)  
        results[5] = np.dot(s * self.field_s[xx][yy][z_next] *  np.dot(self.field_u[2][xx][yy][z_next], self.field_r[xx][yy][z_next]), r.T)  
         
        for result in results:   
            
            bond_energy += self.j_one * result[0][0]; 
            bond_energy += self.j_two * result[1][1]; 
            bond_energy += self.j_three * result[2][2];  
        return bond_energy