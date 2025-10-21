import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave():
    # Generate time values from 0 to 1 with small intervals
    t = np.arange(0, 1, 0.001)
    # Set the frequency of the sine wave (you can change this)
    frequency = 5
    # Calculate the sine wave
    y = np.sin(2 * np.pi * frequency * t)

    # Plot the sine wave
    plt.plot(t, y)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Sine Wave')
    plt.show()

if __name__ == "__main__":
    plot_sine_wave()
