#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 02:10:00 2020

@author: yurifarod
"""
from scipy.stats import friedmanchisquare, kruskal, wilcoxon
import matplotlib.pyplot as plt

cost_hill = [3420.52744873, 3897.78744873, 3108.76744873, 2909.94744873, 2942.82744873,
 3614.90744873, 2856.44744873, 3706.42744873, 2855.72744873, 3998.82744873]
cost_simulated = [3174.14744873, 2558.12744873, 3279.66744873, 2892.84744873, 3476.66744873,
 3206.52744873, 3122.62744873, 3477.56744873, 3499.40744873, 3545.82744873]
cost_tabu = [2997.28744873, 2846.90744873, 3066.22744873, 3406.54744873, 2797.42744873,
 2714.56744873, 3453.74744873, 3647.98744873, 2900.22744873, 3464.18744873]
cost_genetico = [1762.24744873, 1571.70744873, 1675.18744873, 1757.10744873, 1658.16744873,
 1633.30744873, 2104.36744873, 1787.08744873, 1736.04744873, 1540.66744873]

print(friedmanchisquare(cost_hill, cost_simulated, cost_tabu, cost_genetico))
print(kruskal(cost_hill, cost_simulated, cost_tabu, cost_genetico))
print(wilcoxon(cost_genetico, cost_tabu))

  
# Creating plot 
data = ([cost_hill, cost_simulated, cost_tabu, cost_genetico])
plt.boxplot(data) 
  
# show plot 
plt.show()