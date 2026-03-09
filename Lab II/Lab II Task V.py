# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:10:34 2026

@author: rares
"""

# Task I:   Make a simulation using the logistic regression expression for population growth. 
#           Use a growth factor r=0.9. Write a short report that describes the fate of the population when r=0.9.

# Task II:  Use your simulation to point out at what value of r the population growth becomes chaotic. 
#           Show your result with a screenshot.

# Task III: For each value of r, calculate the population size and plot the data:
#           r = [2,2.5,1,1.2,3.1,0.5,4,4.4,3,2.9,2.8,1.9,1.5,1.4,7,3.8,8]

# Task IV:  Consider the above vector as values for r factor, measured here, across 17 years. 
#           Answer the question what will the pupulation growth be in year 17?

# Task V:   Make a series of experiments i which the population number starts from a) 0.1 b) 0.5 c) 1.0 d) 2
#           Make a report in which you note the observations from r = 4.

import matplotlib.pyplot as plt

plt.close('all')

initial_values = [0.1, 0.5, 1.0, 2.0]

r = 4
steps = 50

for initial_population in initial_values:

    print("\n==============================")
    print(f"Experiment with initial population = {initial_population}")
    print("==============================")

    population = initial_population
    populations = []

    for step in range(steps):
        populations.append(population)

        print(f"Step {step}: population = {population:.5f}")

        population = r * population * (1 - population)

    plt.figure(figsize=(8,5))
    plt.plot(range(steps), populations, marker='o')

    plt.xlabel("Time step")
    plt.ylabel("Population")
    plt.title(f"Logistic Growth (r = 4, initial population = {initial_population})")
    plt.grid(True)

plt.show()
