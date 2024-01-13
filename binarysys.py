import numpy

## Constants
m_sol = (1.98847+0.00007)* 10**30
G = 6.67430 * 10**(-11)
c = 299792458

# NOTE: ADD SOMETHING FOR CHIRP MASS

#** MASSES IN SOLAR MASSES
class celestialBody:
    def __init__(self, btype, mass, angular_momentum, position, volume=None):
        # kg, m^3, kg m^2/s
        self.btype = btype
        self.mass = mass 
        self.volume = volume
        self.position = tuple(position) # (x,y)
        self.angular_momentum = tuple(angular_momentum)

        # For the case of a black hole, we do not have defined volume, we instead have volume defined as the Schwarz Rad
        if self.btype=="BH":
            self.volume = 2 * G * self.mass / c**2
            
    def __str__(self):
        return f"celestialBody(btype={self.btype}, mass={self.mass}, volume={self.volume}, angular_momentum={self.angular_momentum})"

