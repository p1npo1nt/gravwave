import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.integrate import odeint
import binarysys as bs

# Constants and ranges for our grid in space
x = np.linspace(-100, 100, 400)
y = np.linspace(-100, 100, 400)
X, Y = np.meshgrid(x, y)
G = 6.67430e-11  

cb1 = bs.celestialBody(btype="BH", mass=30e12, angular_momentum=.9, position=(-30,0))
cb2 = bs.celestialBody(btype="BH", mass=35e12, angular_momentum=.7, position=(30,0))

def binary_gravitational_potential(X, Y, mass1, mass2, pos1, pos2):
    r1 = np.sqrt((X- cb1.position[0])**2 + (Y- cb1.position[1])**2)
    r2 = np.sqrt((X- cb2.position[0])**2 + (Y- cb2.position[1])**2)
    V = -G * (cb1.mass / r1 + cb2.mass / r2)
    return V

# arb. units
mass1 = mass2 = 1e12  # masses of two bodies 
pos1 = (-30, 0)  # position of first body
pos2 = (30, 0)   # position of second body

# computation of gravitational potential
V = binary_gravitational_potential(X, Y, mass1, mass2, pos1, pos2)

# compute the curvature of spacetime (proportional to the potential for the sake fo simplicity)
curvature = V

# Plotting the contour map
plt.figure(figsize=(10, 8))

# Use the curvature to determine the colors (red for high curvature, blue for low)
colors = cm.RdYlBu_r(np.interp(curvature, (curvature.min(), curvature.max()), (0, 1)))

# Plot the contour map with colors based on curvature
contour = plt.contourf(X, Y, curvature, 50, cmap='RdYlBu_r')
plt.colorbar(contour)

# Mark the binary system with red dots
plt.plot(pos1[0], pos1[1], 'ro')
plt.plot(pos2[0], pos2[1], 'ro')

# Annotations for the binary system
plt.annotate('Mass 1', xy=pos1, xytext=(pos1[0]+5, pos1[1]+10),
             arrowprops=dict(facecolor='white', shrink=0.05))
plt.annotate('Mass 2', xy=pos2, xytext=(pos2[0]+5, pos2[1]+10),
             arrowprops=dict(facecolor='white', shrink=0.05))

# Set the aspect of the plot to be equal
plt.axis('equal')

# Set the title and labels
plt.title('Contour Map of Spacetime Curvature Due to a Binary System')
plt.xlabel('x coordinate')
plt.ylabel('y coordinate')

# Show the plot
plt.show()
