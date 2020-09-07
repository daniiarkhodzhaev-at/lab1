#!/usr/bin/python3

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

N = 5

line = None
fig, ax = plt.subplots()

def plt_init() -> int:
    global fig
    N = int(input("N = "))
    plt.xlim([-1.1, 1.1])
    plt.ylim([-1.1, 1.1])
    plt.autoscale(enable=False)
    return 0

def pent_animation(fr=360, inter=50):
    global fig, line

    def init():
        return line

    def animate(frame):
        _x = []
        _y = []
        for i in range(N + 1):
            _x.append(np.cos(2 * np.pi * i / N + frame * np.pi / 180))
            _y.append(np.sin(2 * np.pi * i / N + frame * np.pi / 180))
        line.set_data(_x, _y)
        return line

    return animation.FuncAnimation(fig, animate, init_func=init, frames=fr, interval=inter, repeat=True)

def main() -> int:
    global line, fig, ax

    plt_init()
    ax.set_aspect("equal", adjustable="box")

    line, = ax.plot([], [], "b-")
    _ = pent_animation(360, 50)
    plt.show()
    return 0

if (__name__ == "__main__"):
    main()
