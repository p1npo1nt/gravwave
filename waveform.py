import numpy as np
import matplotlib.pyplot as plt
from pycbc.waveform import get_td_waveform

# Define parameters for the binary system
mass1 = 10.0
mass2 = 5.0
distance = 100.0
inclination = np.pi / 3.0

# Generate a time-domain waveform
hp, hc = get_td_waveform(approximant="SEOBNRv4", mass1=mass1, mass2=mass2,
                          distance=distance, inclination=inclination,
                          delta_t=1.0/4096, f_lower=20)

# Calculate the maximum absolute value of the waveform
amplitude = max(abs(hp))

# Calculate the frequency (inverse of the time between samples)
frequency = 1.0 / hp.delta_t

# Extract the length of the waveform
waveform_length = len(hp)

# Calculate the wavelength (total time duration divided by length)
wavelength = waveform_length * hp.delta_t

# Plot the waveform
plt.figure(figsize=(12, 4))
plt.plot(hp.sample_times, hp, label='Plus polarization')
plt.xlabel('Time (s)')
plt.ylabel('Strain')
plt.legend()

# Create a spectrogram
plt.figure(figsize=(12, 4))
plt.specgram(hp, Fs=1.0/hp.delta_t, cmap='viridis')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Spectrogram')
plt.colorbar(label='Amplitude (Strain)')

plt.show()

# Display amplitude, frequency, and wavelength
print(f"Amplitude: {amplitude}")
print(f"Frequency: {frequency} Hz")
print(f"Wavelength: {wavelength} seconds")
