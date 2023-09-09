# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 10:11:15 2023

@author: Dongli
"""

class StatisticsSolver:
    def mean(self, data):
        return sum(data) / len(data)

    def median(self, data):
        data.sort()
        if len(data)

    def mode(self, data):
        pass

    def variance(self, data):
        pass

    def standard_deviation(self, data):
        pass


# Example Usage:
solver = StatisticsSolver()

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mean_value = solver.mean(data)
median_value = solver.median(data)
mode_value = solver.mode(data)
variance_value = solver.variance(data)
std_deviation_value = solver.standard_deviation(data)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_deviation_value}")
