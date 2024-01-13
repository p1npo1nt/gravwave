import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation
from pycbc.waveform import get_td_waveform

# Constants and ranges for the grid in space for the contour map
x = np.linspace(-100, 100, 400)
y = np.linspace(-100, 100, 400)
X, Y = np.meshgrid(x, y)

# Parameters for the gravitational wave
m1 = 30  # Mass of the first celestial body in solar masses
m2 = 30  # Mass of the second celestial body in solar masses
spin1 = [0, 0, 0.9]  # Dimensionless spin of CB1 aligned with orbital angular momentum
spin2 = [0, 0, -0.9] # Dimensionless spin of CB2 aligned with orbital angular momentum
distance = 500  # Distance to the binary in megaparsecs
inclination = 0  # Inclination angle
f_lower = 20  # Starting frequency of the waveform

# Generate the waveform
hp, hc = get_td_waveform(approximant='SEOBNRv4_opt',
                         mass1=m1,
                         mass2=m2,
                         spin1z=spin1[-1],
                         spin2z=spin2[-1],
                         delta_t=1.0/4096,
                         f_lower=f_lower,
                         distance=distance,
                         inclination=inclination)


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

# Compute the initial potential and curvature
V = binary_gravitational_potential(X, Y, mass1, mass2, pos1, pos2)
curvature = V

# Set up the figure and subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Contour plot setup
contour = ax1.contourf(X, Y, curvature, 50, cmap='RdYlBu_r')
cb = fig.colorbar(contour, ax=ax1)
cb.set_label('Spacetime Curvature')
ax1.plot(pos1[0], pos1[1], 'ro')
ax1.plot(pos2[0], pos2[1], 'ro')
ax1.set
# Set the aspect of the plot to be equal
ax1.axis('equal')

# Set the title and labels for the first subplot
ax1.set_title('Contour Map of Spacetime Curvature Due to a Binary System')
ax1.set_xlabel('x coordinate')
ax1.set_ylabel('y coordinate')

# Waveform plot setup
line, = ax2.plot([], [], label='h+')
ax2.set_xlim(-0.1, 0.1)  # Set a suitable x range that corresponds to your data
ax2.set_ylim(-1e-21, 1e-21)  # Set a suitable y range that corresponds to your data
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Strain')
ax2.legend()
ax2.set_title('Gravitational Waveform')

# Generate the initial waveform data
waveform_time = hp.sample_times.numpy()
waveform_data = hp.numpy()

# Initialize the data for the waveform plot
def init():
    line.set_data([], [])
    return line,

# Define the update function for the animation
def update(frame):
    # Update the curvature with some time dependence for visualization
    curvature_time = curvature * np.cos(frame / 10.0)
    ax1.clear()
    ax1.contourf(X, Y, curvature_time, 50, cmap='RdYlBu_r')
    ax1.plot(pos1[0], pos1[1], 'ro')
    ax1.plot(pos2[0], pos2[1], 'ro')
    ax1.set_title('Contour Map of Spacetime Curvature Due to a Binary System')
    ax1.set_xlabel('x coordinate')
    ax1.set_ylabel('y coordinate')
    ax1.axis('equal')
    
    # Update the waveform plot
    current_time = waveform_time + frame / 30.0  # Adjust the time shift as needed
    current_data = np.interp(current_time, waveform_time, waveform_data)
    line.set_data(current_time, current_data)
    
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=300, init_func=init, blit=True, interval=20)

# Display the animation
plt.show()
