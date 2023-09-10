# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 10:11:15 2023

@author: Dongli
"""

import math

class StatisticsSolver:
    def max_decimal_places(self, nums):
        max_places = 0
        for num in nums:
            if '.' in str(num):
                decimal_places = len(str(num).split('.')[1])
                max_places = max(max_places, decimal_places)
        return max_places
    
    def mean(self, data):
        mean = sum(data) / len(data)
        decimal_places = self.max_decimal_places(data)
        mean = round(mean, decimal_places + 1)
        return mean

    def median(self, data):
        data.sort()
        n = len(data)
        decimal_places = self.max_decimal_places(data)
        if n%2 == 0:
            median = (data[n//2-1] + data[n//2])/2
            median = round(median, decimal_places + 1)
        else:
            median = data[(n-1)//2]
        return median

    def mode(self, data):
        frequency_dict = {}
        for num in data:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        max_frequency = max(frequency_dict.values())
        mode_values = [num for num, frequency in frequency_dict.items() if frequency == max_frequency]
        
        if max_frequency == 1 or len(mode_values) == len(data):
            return "No mode"
        elif len(mode_values) == 1:
            return mode_values[0]
        else:
            return mode_values

    def variance_p(self, data):
        mean = self.mean(data)
        var_list = [(x-mean)*(x-mean) for x in data]
        variance = sum(var_list)/len(data)
        decimal_places = self.max_decimal_places(data)
        variance = round(variance, decimal_places+1)
        return variance

    def variance_s(self, data):
        mean = self.mean(data)
        var_list = [(x-mean)*(x-mean) for x in data]
        variance = sum(var_list)/(len(data)-1)
        decimal_places = self.max_decimal_places(data)
        variance = round(variance, decimal_places+1)
        return variance
    
    def standard_deviation_p(self, data):
        mean = self.mean(data)
        var_list = [(x-mean)*(x-mean) for x in data]
        variance = sum(var_list)/len(data)
        sd = math.sqrt(variance)
        decimal_places = self.max_decimal_places(data)
        sd = round(sd, decimal_places+1)
        return sd

    def standard_deviation_s(self, data):
        mean = self.mean(data)
        var_list = [(x-mean)*(x-mean) for x in data]
        variance = sum(var_list)/(len(data)-1)
        sd = math.sqrt(variance)
        decimal_places = self.max_decimal_places(data)
        sd = round(sd, decimal_places+1)
        return sd
    
    def range(self, data):
        return max(data) - min(data)
    
    def midrange(self, data):
        mr = (max(data) + min(data))/2
        decimal_places = self.max_decimal_places(data)
        mr = round(mr, decimal_places+1)
        return mr

    def weighted_mean(self, data, weights):
        weighted_values = [(data[i] * weights[i]) for i in range(len(data)-1)]
        weighted_mean = sum(weighted_values)/sum(weights)
        decimal_places = self.max_decimal_places(data)
        weighted_mean = round(weighted_mean, decimal_places+1)
        return weighted_mean
    
    def z_score_p(self, data, x):
        mean = sum(data) / len(data)
        var_list = [(x-mean)*(x-mean) for x in data]
        variance = sum(var_list)/len(data)
        sd = math.sqrt(variance)
        z = round((x - mean)/sd, 2)
        return z
    
    def z_score_s(self, data, x):
        mean = sum(data) / len(data)
        var_list = [(x-mean)*(x-mean) for x in data]
        variance = sum(var_list)/(len(data)-1)
        sd = math.sqrt(variance)
        z = round((x - mean)/sd, 2)
        return z
    
    def percentile_get_p(self, data, x):
        data.sort()
        i = data.index(x)
        p = (i + 0.5) * 100 / len(data)
        p = round(p, 2)
        return p
    
    def percentile_get_x(self, data, p):
        data.sort()
        i = (p * len(data) / 100) - 0.5
        i = round(i)
        return data[i]
    
    
# Example Usage:
solver = StatisticsSolver()

data = [1, 2, 3, 4, 8, 8, 7, 6, 7, 9, 10]
weights = [2, 4, 5, 1, 9, 3, 4, 6, 8, 3, 8]
x = 8
p = 40

mean_value = solver.mean(data) 
median_value = solver.median(data)
mode_value = solver.mode(data)
variance_value_population = solver.variance_p(data)
variance_value_sample = solver.variance_s(data)
sd_value_population = solver.standard_deviation_p(data)
sd_value_sample = solver.standard_deviation_s(data)
data_range = solver.range(data)
midrange = solver.midrange(data)
weighted_mean = solver.weighted_mean(data, weights)
z_population = solver.z_score_p(data, x)
z_sample = solver.z_score_s(data, x)
get_percentile = solver.percentile_get_p(data, x)
get_value_from_p = solver.percentile_get_x(data, p)


print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Variance p: {variance_value_population}")
print(f"Variance s: {variance_value_sample}")
print(f"Standard deviation population: {sd_value_population}")
print(f"Standard deviation sample: {sd_value_sample}")
print(f"Range: {data_range}")
print(f"Midrange: {midrange}")
print(f"Weighted mean: {weighted_mean}")
print(f"z score population: {z_population}")
print(f"z score sample: {z_sample}")
print(f"Percentile of {x}: {get_percentile}")
print(f"value when p = {p}: {get_value_from_p}")


