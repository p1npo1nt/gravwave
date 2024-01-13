import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.integrate import odeint
import binarysys as bs
from pycbc.waveform import get_td_waveform

# Constants and ranges for our grid in space
x = np.linspace(-100, 100, 400)
y = np.linspace(-100, 100, 400)
X, Y = np.meshgrid(x, y)
G = 6.67430e-11  

cb1 = bs.celestialBody(btype="BH", mass=30e12, angular_momentum=(.9,.6), position=(-30,0))
cb2 = bs.celestialBody(btype="BH", mass=35e12, angular_momentum=(.7,.4), position=(30,0))

hp, hc = get_td_waveform(
    approximant='SEOBNRv4_opt',
    mass1=cb1.mass,
    mass2=cb2.mass,
    spin1z=cb1.angular_momentum[0],
    spin2z=cb2.angular_momentum[0],
    # spin1y=cb1.angular_momentum[1],
    # spin2y=cb2.angular_momentum[1],
    f_lower=20, # starting freq of 20hz as per standards from LIGO
    delta_t=0.00024,
    distance=500,
    inclination=0,
)


# convert to numpy array
hp_data=hp.numpy()
hc_data=hc.numpy()
sample_times=hp.sample_times

plt.tight_layout()

plt.figure(figsize=(10, 6))
# Plot hp (h+)
plt.subplot(2, 1, 1)
plt.specgram(hp_data, Fs=1.0 / hp.delta_t, cmap='viridis')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Spectrogram of h+ (hp, h-plus) Polarization')

# Plot hc (h-cross)
plt.subplot(2, 1, 2)
plt.specgram(hc_data, Fs=1.0 / hc.delta_t, cmap='viridis')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Spectrogram of hx (hc, h-cross) Polarization')


plt.show()
