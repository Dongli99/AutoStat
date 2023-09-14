from AutoStat import *

# Example Usage:
solver = StatisticsSolver()

data = [94, 86, 82, 81, 87, 77, 73, 62, 60, 57, 2]
weights = [2, 4, 5, 1, 9, 3, 4, 6, 8, 3, 2, 4, 5, 1, 9, 3, 4, 6, 
           8, 3, 2, 4, 5, 1, 9, 3, 4, 6, 8, 3]
x = 2
p = 90
a = 10
b = 90

mean_value = solver.mean(data) 
median_value = solver.median(data)
mode_value = solver.mode(data)
variance_value_population = solver.variance_p(data)
variance_value_sample = solver.variance_s(data)
sd_value_population = solver.standard_deviation_p(data)
sd_value_sample = solver.standard_deviation_s(data)
data_range = solver.range(data)
midrange = solver.midrange(data)
# weighted_mean = solver.weighted_mean(data, weights)
z_population = solver.z_score_p(data, x)
z_sample = solver.z_score_s(data, x)
get_percentile = solver.percentile_get_p(data, x)
get_percentile
get_value_from_p = solver.percentile_get_x(data, p)
quartiles = solver.quartile_and_more(data)
a2b_percentile_range = solver.a2b_percentile_range(data, a, b)
outlier_check = solver.outlier_check(data, x)


print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Variance p: {variance_value_population}")
print(f"Variance s: {variance_value_sample}")
print(f"Standard deviation population: {sd_value_population}")
print(f"Standard deviation sample: {sd_value_sample}")
print(f"Range: {data_range}")
print(f"Midrange: {midrange}")
# print(f"Weighted mean: {weighted_mean}")
print(f"z score population of {x}: {z_population}")
print(f"z score sample of {x}: {z_sample}")
print(f"Percentile of {x}: {get_percentile}")
print(f"value when p = {p}: {get_value_from_p}")
print("Quartiles:")
solver.print_dict(quartiles)
print(f"P{a} to P{b} percentile range: {a2b_percentile_range}")
print(f'{x} is {outlier_check}')

 
