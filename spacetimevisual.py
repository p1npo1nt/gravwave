import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.integrate import odeint

# Constants and ranges for our grid in space
x = np.linspace(-100, 100, 400)
y = np.linspace(-100, 100, 400)
X, Y = np.meshgrid(x, y)

# Function to describe the gravitational potential of a binary system
def binary_gravitational_potential(X, Y, mass1, mass2, pos1, pos2):
    # Gravitational constant
    G = 6.67430e-11  
    # Potential due to mass1 and mass2
    r1 = np.sqrt((X-pos1[0])**2 + (Y-pos1[1])**2)
    r2 = np.sqrt((X-pos2[0])**2 + (Y-pos2[1])**2)
    V = -G * (mass1 / r1 + mass2 / r2)
    return V

# Masses and positions of the two bodies (in arbitrary units)
mass1 = mass2 = 1e12  # Masses of the two bodies
pos1 = (-30, 0)  # Position of the first body
pos2 = (30, 0)   # Position of the second body

# Compute the potential
V = binary_gravitational_potential(X, Y, mass1, mass2, pos1, pos2)

# Compute the curvature of spacetime (which is proportional to the potential in our simple model)
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
