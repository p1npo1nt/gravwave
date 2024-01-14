import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import matplotlib.patches as patches
import binarysys as bs


def run_simulation(m, spin, sep):
    cb1 = bs.celestialBody(btype="BH", mass=m[0], angular_momentum=spin[0], position=(30,0))
    cb2 = bs.celestialBody(btype="BH", mass=m[1], angular_momentum=spin[1], position=(-30,0))

    # constants for the orbit
    orbit_radius = sep
    orbit_center_x = 0
    orbit_center_y = 0
    orbit_period = 2 * np.pi 


    # gens contour plot data
    def generate_data(x1, y1, x2, y2, mass1, mass2):
        xpos = np.linspace(-75, 75, 100)  
        ypos = np.linspace(-50, 50, 100)  
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

    sam1 = 20  
    sam2 = 15  
    ecc1 = 0.3  # eccentricity for cb1
    ecc2 = 0.5  # eccentricity for cb2
    
    def get_orbit_radius(angular_momentum, mass, velocity):
        return angular_momentum / (mass * velocity)
    
    def plot_orbit(ax, center_x, center_y, semi_major_axis, semi_minor_axis, color='gray', linestyle='--'):
        ellipse = patches.Ellipse((center_x, center_y), 2*semi_major_axis, 2*semi_minor_axis, fill=False, color=color, linestyle=linestyle)
        ax.add_artist(ellipse)
    
    # constant velocity
    v1 = 20
    v2 = 20
    
    orbit_radius1 = get_orbit_radius(spin[0][0], m[0], v1)  
    orbit_radius2 = get_orbit_radius(spin[1][0], m[1], v2)
    
    semi_minor_axis1 = orbit_radius1 * 0.7  # Example value, adjust as needed
    semi_minor_axis2 = orbit_radius2 * 0.7

    def elliptical_orbit(semi_major_axis, eccentricity, angle):
        r = (semi_major_axis * (1 - eccentricity ** 2)) / (1 + eccentricity * np.cos(angle))
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        return x, y
    
    # Create the initial contour plot
    T, D, Z = generate_data(x1, y1, x2, y2, cb1.mass, cb2.mass)
    fig, ax = plt.subplots()
    
    plot_orbit(ax, orbit_center_x, orbit_center_y, orbit_radius1, semi_minor_axis1, color='blue', linestyle='-')
    plot_orbit(ax, orbit_center_x, orbit_center_y, orbit_radius2, semi_minor_axis2, color='red', linestyle='-')
    
    contour = ax.contourf(T, D, Z, levels=50, cmap='plasma', title='Mass influence on spacetime')
    plt.colorbar(contour)
    plt.title(f'Mass={cb1.mass,cb2.mass} msol, SpinZ={cb1.angular_momentum[0],cb2.angular_momentum[0]}, Sep={sep} au')
    plt.xlabel("x-pos (au)")
    plt.ylabel("y-pos (au)")

    # white points; center
    point1, = ax.plot(x1, y1, 'wo')  
    point2, = ax.plot(x2, y2, 'wo')  

    
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

    animation = FuncAnimation(fig, update, frames=np.linspace(0, orbit_period, 100), blit=False)

    # Show the animated plot
    plt.show()


if __name__ == "__main__":
    pass
