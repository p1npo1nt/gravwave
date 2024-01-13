import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from matplotlib import cm
import binarysys as bs

# Constants and ranges for our grid in space
x = np.linspace(-100, 100, 400)
y = np.linspace(-100, 100, 400)
X, Y = np.meshgrid(x, y)
G = 6.67430e-11

# Create instances of celestial bodies
cb1 = bs.celestialBody(btype="BH", mass=30e12, angular_momentum=.9, position=(-30, 0))
cb2 = bs.celestialBody(btype="BH", mass=35e12, angular_momentum=.7, position=(30, 0))

# Define the binary_gravitational_potential function here
def binary_gravitational_potential(X, Y, mass1, mass2, pos1, pos2):
    r1 = np.sqrt((X - pos1[0]) ** 2 + (Y - pos1[1]) ** 2)
    r2 = np.sqrt((X - pos2[0]) ** 2 + (Y - pos2[1]) ** 2)
    V = -G * (mass1 / r1 + mass2 / r2)
    return V

# Computation of gravitational potential
V = binary_gravitational_potential(X, Y, cb1.mass, cb2.mass, cb1.position, cb2.position)

# Initialize the figure for animation
fig, ax = plt.subplots(figsize=(10, 8))
contour = ax.contourf(X, Y, V, 50, cmap='RdYlBu_r')
colorbar = plt.colorbar(contour)

# Initialize the celestial bodies on the plot
body1, = ax.plot([], [], 'ro')
body2, = ax.plot([], [], 'ro')

# Function to update the animation
def update(frame):
    # Move the celestial bodies in their orbit
    cb1.update_position(frame)
    cb2.update_position(frame)

    # Update the positions on the plot
    body1.set_data(cb1.position[0], cb1.position[1])
    body2.set_data(cb2.position[0], cb2.position[1])

    # Recalculate the gravitational potential with new positions
    V = binary_gravitational_potential(X, Y, cb1.mass, cb2.mass, cb1.position, cb2.position)

    # Update the contour plot
    contour = ax.contourf(X, Y, V, 50, cmap='RdYlBu_r')

    # Redraw the annotations and titles to match the updated plot
    ax.annotate('Mass 1', xy=cb1.position, xytext=(cb1.position[0] + 5, cb1.position[1] + 10),
                 arrowprops=dict(facecolor='white', shrink=0.05))
    ax.annotate('Mass 2', xy=cb2.position, xytext=(cb2.position[0] + 5, cb2.position[1] + 10),
                 arrowprops=dict(facecolor='white', shrink=0.05))
    ax.set_title('Contour Map of Spacetime Curvature Due to a Binary System')
    ax.set_xlabel('x coordinate')
    ax.set_ylabel('y coordinate')
    ax.axis('equal')

    return contour.collections + [body1, body2]

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 1), interval=50)

# Add a slider to control the animation
ax_slider = plt.axes([0.2, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, 'Time', 0, 100, valinit=0)

# Function to update the animation with the slider
def update_slider(val):
    frame = int(val)
    update(frame)

# Connect the slider to the update_slider function
slider.on_changed(update_slider)

# Show the animation
plt.show()
