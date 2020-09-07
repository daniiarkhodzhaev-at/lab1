#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

STEP = 1000
N = 100

a = 3
b = 0.1

def w(x: np.ndarray) -> np.ndarray:
    summ = np.ndarray(len(x))
    for i in range(N):
        summ += b ** i * np.cos(a ** i * np.pi * x)
    return summ

def main() -> int:
    _x = np.array(range(-5 * STEP, 5 * STEP)) / STEP
    _y = w(_x)
    plt.plot(_x, _y)
    plt.show()
    return 0

if (__name__ == "__main__"):
    main()
