import numpy

## Constants
m_sol = (1.98847+0.00007)* 10**30
G = 6.67430 * 10**(-11)
c = 299792458

class celestialBody:
    def __init__( self, btype, mass, angular_momentum, volume=None):
        # kg, m^3, kg m^2/s
        self.btype = btype
        self.mass = mass 
        self.volume = volume
        self.angular_momentum = angular_momentum

        # For the case of a black hole, we do not have defined volume, we instead have volume defined as the Schwarz Rad
        if self.btype=="BH":
            self.volume = 2 * G * self.mass / c**2
            
    def __str__(self):
        return f"celestialBody(btype={self.btype}, mass={self.mass}, volume={self.volume}, angular_momentum={self.angular_momentum})"

# initilization of cb1 and cb2
cb1 = celestialBody(btype="BH", mass=30*m_sol, angular_momentum=.9)
cb2 = celestialBody(btype="BH", mass=35*m_sol, angular_momentum=.7)

print(cb1,cb2)