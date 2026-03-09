# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:24:19 2026

@author: rares
"""

# Task 6:   Modify the value of the weight for state B to 0.5.
#           Plot the evolution of the population for 15 steps based on sequence S. 
# Answer the question: Does the population survive after 15 steps?

import matplotlib.pyplot as plt

plt.close('all')

S = ['A','C','C','C','C','A','C','A','C','C','C','C','A','C','B']

weights = {
    'A': 1.5,
    'B': 0.5,
    'C': 3.3
}

population = 0.5
populations = [population]

print("Step | State | r value | Population")
print("------------------------------------")

for step, state in enumerate(S, start=1):

    r = weights[state]
    population = r * population * (1 - population)

    populations.append(population)

    print(f"{step:>4} |   {state}   |  {r:>4}   | {population:.5f}")

plt.figure(figsize=(10,6))
plt.plot(range(len(populations)), populations, marker='o')

plt.xlabel("Step")
plt.ylabel("Population")
plt.title("Population Evolution for 15 Steps (B weight = 0.5)")
plt.grid(True)

plt.show()

if populations[-1] > 0:
    print("\nAnswer: The population survives after 15 steps.")
else:
    print("\nAnswer: The population does not survive after 15 steps.")
