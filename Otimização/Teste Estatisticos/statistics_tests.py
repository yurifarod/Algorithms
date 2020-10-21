#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 02:10:00 2020

@author: yurifarod
"""
from scipy.stats import friedmanchisquare, kruskal, wilcoxon

costs_max_hill_climbing_sphere = [3067, 2421, 2547, 2560, 2539, 2838, 3030, 2531, 2237, 2049]
costs_max_simulated_annealing_sphere = [2498, 2279, 2305, 3031, 1963, 2947, 2829, 2140, 2419, 1963]
costs_max_search_tabu_sphere = [2900, 2197, 2923, 2556, 2617, 2704, 2736, 2664, 2587, 2606]

costs_max_hill_climbing_rosenbrock = [2054, 1367, 2937, 973, 1649, 3429, 1888, 3546, 5351, 3349]
costs_max_simulated_annealing_rosenbrock = [1907, 542, 1445, 1456, 2176, 1673, 2918, 2223, 1927, 1456]
costs_max_search_tabu_rosenbrock = [2487, 2580, 1363, 3666, 2057, 2392, 2093, 2660, 2641, 1794]

print(friedmanchisquare(costs_max_hill_climbing_sphere, costs_max_simulated_annealing_sphere, costs_max_search_tabu_sphere))
print(kruskal(costs_max_hill_climbing_sphere, costs_max_simulated_annealing_sphere, costs_max_search_tabu_sphere))
print(wilcoxon(costs_max_hill_climbing_sphere, costs_max_simulated_annealing_sphere))
print(wilcoxon(costs_max_hill_climbing_sphere, costs_max_search_tabu_sphere))
print(wilcoxon(costs_max_simulated_annealing_sphere, costs_max_search_tabu_sphere))
print()
print(friedmanchisquare(costs_max_hill_climbing_rosenbrock, costs_max_simulated_annealing_rosenbrock, costs_max_search_tabu_rosenbrock))
print(kruskal(costs_max_hill_climbing_rosenbrock, costs_max_simulated_annealing_rosenbrock, costs_max_search_tabu_rosenbrock))
print(wilcoxon(costs_max_hill_climbing_rosenbrock, costs_max_simulated_annealing_rosenbrock))
print(wilcoxon(costs_max_hill_climbing_rosenbrock, costs_max_search_tabu_rosenbrock))
print(wilcoxon(costs_max_simulated_annealing_rosenbrock, costs_max_search_tabu_rosenbrock))