# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 10:11:15 2023

@author: Dongli
"""

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

    def standard_deviation(self, data):
        pass


# Example Usage:
solver = StatisticsSolver()

data = [1, 2, 3, 4, 8, 8, 7, 6, 7, 9, 10]

mean_value = solver.mean(data)
median_value = solver.median(data)
mode_value = solver.mode(data)
variance_value_population = solver.variance_p(data)
variance_value_sample = solver.variance_s(data)
std_deviation_value = solver.standard_deviation(data)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Variance: {variance_value_population}")
print(f"Variance: {variance_value_sample}")
print(f"Standard Deviation: {std_deviation_value}")
