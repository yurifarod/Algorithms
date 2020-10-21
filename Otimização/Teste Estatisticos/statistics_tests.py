#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 02:10:00 2020

@author: yurifarod
"""
from scipy.stats import friedmanchisquare, kruskal, mannwhitneyu, wilcoxon
import scikit_posthocs as sp

costs_max_hill_climbing_sphere = []
costs_max_simulated_annealing_sphere = []
costs_max_search_tabu_sphere = []

costs_max_hill_climbing_rosenbrock = []
costs_max_simulated_annealing_rosenbrock = []
costs_max_search_tabu_rosenbrock = []

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