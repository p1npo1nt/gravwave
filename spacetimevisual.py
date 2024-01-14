import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import binarysys as bs


def run_simulation(m, spin):
    cb1 = bs.celestialBody(btype="BH", mass=m[0], angular_momentum=spin[0], position=(30,0))
    cb2 = bs.celestialBody(btype="BH", mass=m[1], angular_momentum=spin[1], position=(-30,0))
    # cb3 = bs.celestialBody(btype="BH", mass=15, angular_momentum=(.1, .2), position=(10,10))

    # constants for the orbit
    orbit_radius = 2.5
    orbit_center_x = 0
    orbit_center_y = 0
    orbit_period = 2 * np.pi 


    # gens contour plot data
    def generate_data(x1, y1, x2, y2, mass1, mass2):
        xpos = np.linspace(-20, 20, 100)  # Time axis
        ypos = np.linspace(-20, 20, 100)  # Depth axis
        T, D = np.meshgrid(xpos, ypos)

        # mass influence
        influence1 = mass1 / (np.sqrt((T - x1)**2 + (D - y1)**2) + 1)  # Added 1 to avoid division by zero
        influence2 = mass2 / (np.sqrt((T - x2)**2 + (D - y2)**2) + 1)
        # influence3 = cb3.mass / (np.sqrt((T - x3)**2 + (D - y3)**2) + 1)
        
        Z = influence1 + influence2 # Combined influence
        return T, D, Z

    # initialize the positions of the objects
    x1 = orbit_center_x + orbit_radius
    y1 = orbit_center_y
    x2 = orbit_center_x - orbit_radius
    y2 = orbit_center_y
    # x3 = orbit_center_x + 10
    # y3 = orbit_center_y - 10

    sam1 = 20  # semi-major axis for cb1
    sam2 = 15  # semi-major axis for cb2
    ecc1 = 0.3  # eccentricity for cb1
    ecc2 = 0.5  # eccentricity for cb2

    # Create the initial contour plot
    T, D, Z = generate_data(x1, y1, x2, y2, cb1.mass, cb2.mass)
    fig, ax = plt.subplots()
    contour = ax.contourf(T, D, Z, levels=50, cmap='plasma')
    plt.colorbar(contour)
    plt.xlabel("x-pos")
    plt.ylabel("y-pos")

    # Create two moving points
    point1, = ax.plot(x1, y1, 'wo')  # White point for object
    point2, = ax.plot(x2, y2, 'wo')  # White point for object
    # point3 = ax.plot(x3, y3, 'wo')

    orbit_radius1 = 20 # rad of cb1
    orbit_radius2 = 15 # rad of cb2

    def elliptical_orbit(semi_major_axis, eccentricity, angle):
        r = (semi_major_axis * (1 - eccentricity ** 2)) / (1 + eccentricity * np.cos(angle))
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        return x, y

    # Update function for animation
    def update(frame):
        angle = frame / orbit_period * 2 * np.pi
        x1, y1 = elliptical_orbit(sam1, ecc1, angle)
        x2, y2 = elliptical_orbit(sam2, ecc2, angle + np.pi)

        point1.set_data(x1, y1)
        point2.set_data(x2, y2)

        # Update the contour plot
        T, D, Z = generate_data(x1, y1, x2, y2, cb1.mass, cb2.mass)
        for c in contour.collections:
            c.remove()
        contour = ax.contourf(T, D, Z, levels=50, cmap='plasma')

        return point1, point2, contour

# Set up the animation
    animation = FuncAnimation(fig, update, frames=np.linspace(0, orbit_period, 100), blit=False)

    # Show the animated plot
    plt.show()

# This part allows the script to be run standalone
if __name__ == "__main__":
    # Default values or logic to get values
    pass
