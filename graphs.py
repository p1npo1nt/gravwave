import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from pycbc.waveform import get_td_waveform
import binarysys as bs

def run_simulation(m, spin):
    # This file allows you to plot the waveforms and spectograms of said waveforms via the input of certain parameters for a binary system
    cb1 = bs.celestialBody(btype="BH", mass=m[0], angular_momentum=spin[0], position=(30,0))
    cb2 = bs.celestialBody(btype="BH", mass=m[1], angular_momentum=spin[1], position=(-30,0))

    x = np.linspace(-100, 100, 400)
    y = np.linspace(-100, 100, 400)
    X, Y = np.meshgrid(x, y)
    G = 6.67430e-11

    hp, hc = get_td_waveform(
        approximant='SEOBNRv4_opt',
        mass1=cb1.mass,
        mass2=cb2.mass,
        spin1z=cb1.angular_momentum[0],
        spin2z=cb2.angular_momentum[0],
        f_lower=20,
        delta_t=0.00024,
        distance=500,
        inclination=0,
    )

    sample_times = hp.sample_times
    hp_data = hp.numpy()
    hc_data = hc.numpy()
    phase = np.linspace(0, 2 * np.pi, len(sample_times))

    # Create a single figure with two subplots
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    # Plot h+ (hp) and h-cross (hc) waveforms


    axes[0, 0].plot(sample_times, hp_data, label='h+ polarization')
    axes[0, 0].set_xlabel('Time (s)')
    axes[0, 0].set_ylabel('Strain')
    axes[0, 0].legend()
    axes[0, 0].set_title('h+ (hp, h-plus) Polarization of Gravitational Wave')

    axes[1, 0].plot(sample_times, hc_data, label='hx polarization')
    axes[1, 0].set_xlabel('Time (s)')
    axes[1, 0].set_ylabel('Strain')
    axes[1, 0].legend()
    axes[1, 0].set_title('hx (hc, h-cross) Polarization of Gravitational Wave')

    # spectograms
    axes[0, 1].specgram(hp_data, Fs=1.0 / hp.delta_t, cmap='viridis')
    axes[0, 1].set_xlabel('Time (s)')
    axes[0, 1].set_ylabel('Frequency (Hz)')
    axes[0, 1].set_title('Spectrogram of h+ (hp, h-plus) Polarization')

    axes[1, 1].specgram(hc_data, Fs=1.0 / hc.delta_t, cmap='viridis')
    axes[1, 1].set_xlabel('Time (s)')
    axes[1, 1].set_ylabel('Frequency (Hz)')
    axes[1, 1].set_title('Spectrogram of hx (hc, h-cross) Polarization')

    fig.text(0.02, 0.02, f'CB2\nMass: {cb2.mass}, SpinZ: {cb2.angular_momentum[0]}', fontsize=10)
    fig.text(0.02, 0.5, f'CB1\nMass: {cb1.mass}, SpinZ: {cb1.angular_momentum[0]}', fontsize=10)
    # plt.annotate(f'CB1\nMass: {cb1.mass}, SpinZ: {cb1.angular_momentum[0]}', xycoords='figure points', xy=(1,0))
    # plt.annotate(f'CB2\nMass: {cb2.mass}, SpinZ: {cb2.angular_momentum[0]}', xycoords='figure points', xy=(150,0))

    plt.tight_layout()

    plt.show()
