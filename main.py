# Equation : dy/dx + p(x, y) + q(y) + r(x) = 0

from functions import alpha
from math import pi
import numpy as np
import csv


# initial conditions

x_0 = -0.999999999
x_n = 0.999999999
y_0 = -1
dydx_0 = 10
steps = 10**6


# initialization

x = np.linspace(x_0, x_n, num=(steps + 1))
y = np.zeros(steps + 1)
y_ = np.zeros(steps + 1)
y[0] = y_0
y_[0] = dydx_0
dx = x[1] - x[0]


# workings

for i in range(steps):
    dy_ = -1 * alpha(x[i], y[i], y_[i]) * dx
    y_[i+1] = y_[i] + dy_
    y[i+1] = y[i] + y_[i]*dx

y__ = np.array([-1 * alpha(x[i], y[i], y_[i]) for i in range(steps + 1)])

# saving data

# result_no = int(input("Result No. : "))
file_path = "results.csv"

with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y', 'dy/dx', 'd2y/dx2'])

    for j in range(steps + 1):
        writer.writerow([x[j], y[j], y_[j], y__[j]])
