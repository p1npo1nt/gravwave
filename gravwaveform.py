import numpy as np
import matplotlib.pyplot as plt
from pycbc.waveform import get_td_waveform
# Parameters
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
# Plot the plus polarization of the waveform
plt.figure(figsize=(10, 4))
plt.plot(hp.sample_times, hp, label='h+')
plt.xlabel('Time (s)')
plt.ylabel('Strain')
plt.legend()
plt.show()
