# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:10:34 2026

@author: rares
"""

# Task I:   Make a simulation using the logistic regression expression for population growth. 
#           Use a growth factor r=0.9. Write a short report that describes the fate of the population when r=0.9.

# Task II:  Use your simulation to point out at what value of r the population growth becomes chaotic. 
#           Show your result with a screenshot.

import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

r_values = np.linspace(0, 4, 2000)
x0 = 0.5

r_plot = []
x_plot = []

for r in r_values:
    x = x0

    for i in range(200):
        x = r * x * (1 - x)

    for i in range(100):
        x = r * x * (1 - x)
        r_plot.append(r)
        x_plot.append(x)

print("Population growth becomes chaotic at approximately r ≈ 3.57")

plt.figure(figsize=(10,6))
plt.plot(r_plot, x_plot, 'k.', markersize=0.5)

plt.xlabel("Growth factor r")
plt.ylabel("Population")
plt.title("Logistic Map Chaos")
plt.grid(True)

plt.show()
