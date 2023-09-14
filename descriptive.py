# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 10:11:15 2023

@author: Dongli
"""
from base import StatisticsSolver
import math

class DescriptiveStat(StatisticsSolver): 

    def range(self):
        return max(self.data) - min(self.data)
    
    def midrange(self, is_rounded = True):
        mr = (max(self.data) + min(self.data))/2
        if is_rounded:
            mr = round(mr, self.decimal_places+1)
        return mr
    
    def weighted_mean(self, weights, is_rounded = True):
        weighted_values = [(self.data[i] * weights[i]) for i in range(len(self.data)-1)]
        weighted_mean = sum(weighted_values)/sum(weights)
        if is_rounded:
            weighted_mean = round(weighted_mean, self.decimal_places + 1)
        return weighted_mean
    
    def z_score(self, x):
        # z actually is how many sd away from the mean 
        return round((x - self.mean(False))/self.standard_deviation(False), 2)
    
    def percentile_get_p(self, x):
        # percentile is not related to value, only about order/rank
        return round((self.data.index(x) + 0.5) * 100 / len(self.data))
    
    def percentile_get_x(self, k):
        # given Pk, get x
        # can be performed in R with: quantile(data, probs = 0.4, type = 5)
        position = k * len(self.data) / 100
        if position % 1 == 0:
            # plus 0.5 if whole number, equivalent.
            position = round(position)
            x = (self.data[position - 1] + self.data[position]) / 2
        else:
            # round to next higher whole number
            x = self.data[math.ceil(position) - 1]
        return x
    
    def quartile_and_more(self):
        # this function also follows type 5
        q1 = self.percentile_get_x(25)
        q2 = self.percentile_get_x(50)
        q3 = self.percentile_get_x(75)
        iqr = q3 - q1
        semi_iqr = iqr / 2
        mid_quartile = (q1 + q3) / 2
        mild_boundary = [q1-(1.5*iqr), q3+(1.5*iqr)]
        extreme_boundary = [q1-(3*iqr), q3+(3*iqr)]
        outlier_boundary = f'-ex-<<- ({extreme_boundary[0]}) -<-md-<- ({mild_boundary[0]}) --nm-- ({mild_boundary[1]}) ->-md->- ({extreme_boundary[1]}) ->>-ex-'
        tiles = {
            'Q1': q1, 
            'Q2': q2, 
            'Q3': q3, 
            'IQR': iqr,
            'Semi-interquartile range': semi_iqr,
            'Midquartile': mid_quartile,
            'outlier': outlier_boundary
            }
        return tiles
    
    def a2b_percentile_range(self, a, b):
        a, b = (a, b) if a <= b else (b, a)
        pa = self.percentile_get_x(a)
        pb = self.percentile_get_x(b)
        return pb - pa
    
    def outlier_check(self, x):
        q1 = self.percentile_get_x(25)
        q3 = self.percentile_get_x(75)
        iqr = q3 - q1
        status = ''
        if x > (q3 + (3 * iqr)) or x < (q1 - (3 * iqr)):
            status = "a severe outlier"
        elif x > (q3 + (1.5 * iqr)) or x < (q1 - (1.5 * iqr)):
            status = "a mild outlier"
        else:
            status = "not an outlier"
        return status
    
   
class DescriptiveBivariate:
    
    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list
        self.x_mean = StatisticsSolver(self.x_list).mean(False)
        self.y_mean = StatisticsSolver(self.y_list).mean(False)
        
    def linear_regression(self):
        # will create liniea regression line
        # get m
        sum_x = sum(self.x_list)
        sum_y = sum(self.y_list)
        sum_xy = sum(x * y for x, y in zip(self.x_list, self.y_list))
        sum_x_sq = sum(x * x for x in self.x_list)
        n = len(self.x_list)
        m = (n * sum_xy - (sum_x * sum_y)) / (n * sum_x_sq - (sum_x * sum_x))
        # get b
        b = self.y_mean - (m * self.x_mean)
        # return result
        m = round(m, 3)
        b = round(b, 3)
        line = {'m: ': m, 'b: ': b, 'formula: ': f'y^ = {m}x + {b}'}
        return line
    
    