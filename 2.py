#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

def y(x: np.ndarray) -> np.ndarray:
    return x ** 2 - x - 6

def main() -> int:
    _x = np.array(range(-300,400)) / 100
    _y = y(_x)
    plt.plot(_x, _y)
    plt.show()
    return 0

if (__name__ == "__main__"):
    main()
