#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

STEP = 1000

def main() -> int:
    _x = np.array([1, 2, 3, 4, 5, 6])
    _y = np.array([1, 1.42, 1.76, 2, 2.24, 2.5])

    _xx = np.array(range(0 * STEP, 7 * STEP)) / STEP

    p, v = np.polyfit(_x, _y, deg=1, cov=True)

    plt.errorbar(_x, _y, xerr=0.05, yerr=0.1)

    # plt.plot(_x, _y)
    plt.plot(_xx, np.poly1d(p)(_xx))

    plt.show()

    return 0

if (__name__ == "__main__"):
    main()
