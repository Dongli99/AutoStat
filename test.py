import base
from descriptive import *
from utils import print_dict

# Example Usage:

data = [62,42,19,26,51,15,30,15]
solver = DescriptiveStat(data)

'''
weights = [2, 4, 5, 1, 9, 3, 4, 6, 8, 3, 2, 4, 5, 1, 9, 3, 4, 6, 
           8, 3, 2, 4, 5, 1, 9, 3, 4, 6, 8, 3]
x = 42
p = 90
a = 10
b = 90

mean_value = solver.mean() 
median_value = solver.median()
mode_value = solver.mode()
variance_value_population = solver.variance()
sd_value_population = solver.standard_deviation()
data_range = solver.range()
midrange = solver.midrange()
# weighted_mean = solver.weighted_mean(data, weights)
z_population = solver.z_score(x)
get_percentile = solver.percentile_get_p(x)
get_percentile
get_value_from_p = solver.percentile_get_x(p)
quartiles = solver.quartile_and_more()
a2b_percentile_range = solver.a2b_percentile_range(a, b)
outlier_check = solver.outlier_check(x)


print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Variance p: {variance_value_population}")
print(f"Standard deviation: {sd_value_population}")
print(f"Range: {data_range}")
print(f"Midrange: {midrange}")
# print(f"Weighted mean: {weighted_mean}")
print(f"z score population of {x}: {z_population}")
print(f"Percentile of {x}: {get_percentile}")
print(f"value when p = {p}: {get_value_from_p}") 
print("Quartiles:")
print_dict(quartiles)
print(f"P{a} to P{b} percentile range: {a2b_percentile_range}")
print(f'{x} is {outlier_check}')
'''

# x = [72,69,58,47,84,62,57,45]
# y = [62,42,19,26,51,15,30,15]
x = [1,2,3,4]
y = [2,4,4,6]

bi_v = DescriptiveBivariate(x,y)
regression_line = bi_v.linear_regression()
correlation_coeff = bi_v.correlation_coefficient()
coefficient_of_determination = bi_v.coefficient_of_determination()

print('regression line formula: ')
print_dict(regression_line)
print(f'correlation coeffient: {correlation_coeff}')
print(f'coefficient_of_determination: {coefficient_of_determination}')

 
