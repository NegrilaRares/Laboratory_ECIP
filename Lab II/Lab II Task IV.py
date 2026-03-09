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

# Task IV: Consider the above vector as values for r factor, measured here, across 17 years. 
#          Answer the question what will the pupulation growth be in year 17?

r_values = [2, 2.5, 1, 1.2, 3, 4, 0.5, 4.4, 3.2, 2.9, 2.8, 1.9, 1.5, 1.4, 7, 3.8, 8]

population = 0.5

for year in range(len(r_values)):
    
    r = r_values[year]
    
    population = r * population * (1 - population)
    
    print(f"Year {year+1}: r = {r}, population = {population:.5f}")

print("\nPopulation in year 17 =", round(population,5))
