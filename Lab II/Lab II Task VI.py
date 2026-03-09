# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:24:19 2026

@author: rares
"""

# Task 6: Simulate a Markov-machine containing 3 states A, B, and C:

# A connects to B(0.4) and C(0.6) 
# B connects to A(0.5) , itself(0.5)
# C connects to itself(0.6), A(0.2) and B(0.2)

# in () u find the value on the arrows

# Run this machine 15 times and record the sequence of states. Store these states as "S".

# Each state carries a weight:
# A= 1.5
# B=2
# C=3.3

# Use these weights as values for the growth factor r, 
# and calculate the population size on 15 steps according to the weights from S.
# Start the population from 0.5.

import random

transitions = {
    'A': [('B', 0.4), ('C', 0.6)],
    'B': [('A', 0.5), ('B', 0.5)],
    'C': [('C', 0.6), ('A', 0.2), ('B', 0.2)]
}

weights = {
    'A': 1.5,
    'B': 2.0,
    'C': 3.3
}

steps = 15
population = 0.5
current_state = 'A'

S = [current_state]

for _ in range(steps-1):

    rand_value = random.random()
    cumulative = 0

    for next_state, prob in transitions[current_state]:
        cumulative += prob
        if rand_value <= cumulative:
            current_state = next_state
            break

    S.append(current_state)

print("\nStep | State | r value | Population")
print("------------------------------------")

for i, state in enumerate(S, start=1):

    r = weights[state]
    population = r * population * (1 - population)

    print(f"{i:>4} |   {state}   |  {r:>4}   | {population:.5f}")
