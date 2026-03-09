# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:10:34 2026

@author: rares
"""

# Make a simulation using the logistic regression expression for population growth. 
# Use a growth factor r=0.9. Write a short report that describes the fate of the population when r=0.9.

import matplotlib.pyplot as plt

r = 0.9        
x = 0.5        
steps = 50     

population = [x]

for i in range(steps):
    x = r * x * (1 - x)
    population.append(x)

for i, p in enumerate(population):
    print(f"Step {i}: population = {p:.5f}")

plt.plot(population)
plt.xlabel("Time step")
plt.ylabel("Population")
plt.title("Logistic Population Growth (r = 0.9)")
plt.show()
