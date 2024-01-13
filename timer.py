import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation
from pycbc.waveform import get_td_waveform

# ... (previous code for setting up the gravitational potential and waveform)

# Initialize the figure and axes for the animation
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Initialize the contour plot
# ... (previous code for setting up the contour plot)

# Initialize the waveform plot
# ... (previous code for setting up the waveform plot)

# Initialize the text element for the timer
time_text = ax1.text(0.05, 0.95, '', transform=ax1.transAxes, color='white')

# Function to update the contour plot and waveform for each frame of the animation
def update(frame):
    # Update the spacetime curvature visualization
    # ... (previous code for updating the contour plot)
    
    # Update the gravitational waveform visualization
    # ... (previous code for updating the waveform plot)
    
    # Update the timer text with the current frame's time
    current_time = frame / 30.0  # Assuming 30 frames per second
    time_text.set_text(f'Time: {current_time:.2f}s')
    
    # Return the elements that have changed
    return contour.collections + [line, time_text]

# Create the animation using FuncAnimation
ani = FuncAnimation(fig, update, frames=300, init_func=init, blit=True, interval=20)

# Display the animation
plt.show()
