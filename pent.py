#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

N = 5
OFFSET = 0

def main() -> int:
    plt.xlim([-1.1, 1.1])
    plt.ylim([-1.1, 1.1])
    plt.autoscale(enable=False)
    ax = plt.subplot()
    # ax = fig.add_subplot(111)
    ax.set_aspect("equal", adjustable="box")

    _x = []
    _y = []
    for i in range(N + 1):
        _x.append(np.cos(2 * np.pi * i / N + OFFSET))
        _y.append(np.sin(2 * np.pi * i / N + OFFSET))
    plt.plot(_x, _y)
    plt.show()
    return 0

if (__name__ == "__main__"):
    main()
