from Descriptive import DescriptiveStat
from utils import print_dict
from DescriptiveBivariate import DescriptiveBivariate
from DescriptiveBinomialDis import DescriptiveBinomialDis
from DescriptiveNormalDistribution import DescriptiveNormalDistribution

# Example Usage:

data = [115, 118, 113, 128, 123, 110, 112]
solver = DescriptiveStat(data)

p55 = solver.percentile_get_x(75)
mean = solver.mean()
print(f'mean: {mean}')
median = solver.median()
more = solver.quartile_and_more()
print(f'percentile 55 is: {p55}')
print(f'median of data is: {median}')
print_dict(more)

# x = [72,69,58,47,84,62,57,45]
# y = [62,42,19,26,51,15,30,15]
x = [9, 4, 5, 8, 6, 7]
y = [50, 102, 83, 68, 85, 92]

bi_v = DescriptiveBivariate(x,y)
regression_line = bi_v.linear_regression()
correlation_coeff = bi_v.correlation_coefficient()
coefficient_of_determination = bi_v.coefficient_of_determination(False)

print('regression line formula: ')
print_dict(regression_line)
print(f'correlation coeffient: {correlation_coeff}')
print(f'coefficient_of_determination: {coefficient_of_determination}')

bino = DescriptiveBinomialDis(0.08, 15, 15)
bi_pro = bino.binomial_probability()
print(f'the binomial_probability is {bi_pro}')
bi_mean = bino.bino_prob_mean()
print(f'the probability mean is {bi_mean}')
bi_variance = bino.bino_prob_variance()
print(f'the probability variance is {bi_variance}')
bi_probs = bino.bino_prob_sum(2, 15)
print(f'the probs are {bi_probs}')

nd = DescriptiveNormalDistribution()
ztest = nd.z_score_lookup_lower(-0.01)
print(ztest)

find_z0 = nd.lower_than_z0(0.0002)
print(f'z lower than z0, z0 is {find_z0}')








 
