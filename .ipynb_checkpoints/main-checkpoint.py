import numpy as np
import matplotlib.pyplot as plt

# A - amplitude
# phi - phase
# f - frequency
# N - number of samples
# n - sample index
def generate_harmonic_signal(A, phi, f, N, n):
    return A * np.sin(2 * np.pi * f * n / N + phi)

def task_2A():
    # Option 1 conditions
    A = 10
    f = 2
    N = 2048
    n = np.arange(N)
    phi_options = [0, np.pi/6, np.pi/4, np.pi/2, np.pi]

    for phi in phi_options:
        signal = generate_harmonic_signal(A, phi, f, N, n)
        draw_signal(signal, f"Option 1: phi = {phi}")


def draw_signal(signal, title):
    plt.figure(figsize=(10, 6))
    plt.plot(signal)
    plt.title(title)
    plt.xlabel('Sample index')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    task_2A()

