import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import binarysys as bs

cb1 = bs.celestialBody(btype="BH", mass=20, angular_momentum=(.9, .4), position=(-30,0))
cb2 = bs.celestialBody(btype="BH", mass=15, angular_momentum=(.7, .6), position=(30,0))

# Constants for the orbit
orbit_radius = 2.5
orbit_center_x = 0
orbit_center_y = 0
orbit_period = 2 * np.pi  # One complete orbit


# Create a function that returns the contour plot data
def generate_data(x1, y1, x2, y2, mass1, mass2):
    time = np.linspace(-5, 5, 100)  # Time axis
    depth = np.linspace(-5, 5, 100)  # Depth axis
    T, D = np.meshgrid(time, depth)

    # Influence of each object on spacetime
    influence1 = cb1.mass / (np.sqrt((T - x1)**2 + (D - y1)**2) + 1)  # Added 1 to avoid division by zero
    influence2 = cb2.mass / (np.sqrt((T - x2)**2 + (D - y2)**2) + 1)
    
    Z = influence1 + influence2  # Combined influence
    return T, D, Z

# Initialize the positions of the objects
x1 = orbit_center_x + orbit_radius
y1 = orbit_center_y
x2 = orbit_center_x - orbit_radius
y2 = orbit_center_y

# Create the initial contour plot
T, D, Z = generate_data(x1, y1, x2, y2, cb1.mass, cb2.mass)
fig, ax = plt.subplots()
contour = ax.contourf(T, D, Z, levels=50, cmap='plasma')
plt.colorbar(contour)
plt.xlabel("Time")
plt.ylabel("Depth")

# Create two moving points
point1, = ax.plot(x1, y1, 'wo')  # White point for object
point2, = ax.plot(x2, y2, 'wo')  # White point for object

# Update function for animation
def update(frame):
    # Calculate the new positions for the orbiting points
    angle = frame / orbit_period * 2 * np.pi
    x1 = orbit_center_x + orbit_radius * np.cos(angle)
    y1 = orbit_center_y + orbit_radius * np.sin(angle)
    x2 = orbit_center_x + orbit_radius * np.cos(angle + np.pi)
    y2 = orbit_center_y + orbit_radius * np.sin(angle + np.pi)

    point1.set_data(x1, y1)
    point2.set_data(x2, y2)

    # Update the contour plot for gravitational potential
    T, D, Z = generate_data(x1, y1, x2, y2, cb1.mass, cb2.mass)
    for c in contour.collections:
        c.remove()
    contour = ax.contourf(T, D, Z, levels=50, cmap='plasma')

    return point1, point2, contour

# Set up the animation
animation = FuncAnimation(fig, update, frames=np.linspace(0, orbit_period, 100), blit=False)

# Show the animated plot
plt.show()
