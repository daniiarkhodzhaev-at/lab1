#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def y(x: np.ndarray) -> np.ndarray:
    return np.log(np.exp(1 / (np.sin(x) + 1)) / (5 / 4 + 1 / x ** 15)) / np.log(1 + x ** 2)

def main() -> int:
    print(y(np.array([1, 10, 1000])))
    return 0

if (__name__ == "__main__"):
    main()

