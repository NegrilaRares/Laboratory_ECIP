# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:10:34 2026

@author: rares
"""

# Task I:   Make a simulation using the logistic regression expression for population growth. 
#           Use a growth factor r=0.9. Write a short report that describes the fate of the population when r=0.9.

# Task II:  Use your simulation to point out at what value of r the population growth becomes chaotic. 
#           Show your result with a screenshot.

# Task III:  For each value of r, calculate the population size and plot the data:
#            r = [2,2.5,1,1.2,3.1,0.5,4,4.4,3,2.9,2.8,1.9,1.5,1.4,7,3.8,8]

import matplotlib.pyplot as plt

r_values = [2, 2.5, 1, 1.2, 3.1, 0.5, 4, 4.4, 3, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]

initial_population = 0.5
steps = 50

plt.figure(figsize=(10,6))

for r in r_values:

    population = initial_population
    populations = []

    for step in range(steps):
        populations.append(population)
        population = r * population * (1 - population)

    plt.plot(range(steps), populations, label=f"r = {r}")

plt.xlabel("Time step")
plt.ylabel("Population size")
plt.title("Logistic Population Growth for Different r Values")
plt.legend()
plt.grid(True)

plt.show()
