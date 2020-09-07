#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

STEP = 1000

def y(x: np.ndarray) -> np.ndarray:
    eval(input())
    return x

def main() -> int:
    _x = np.array(range(-10 * STEP, 10 * STEP)) / STEP
    _y = y(_x)
    plt.xkcd()
    plt.plot(_x, _y)
    plt.show()
    return 0

if (__name__ == "__main__"):
    main()
