# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 10:11:15 2023

@author: Dongli
"""
from AutoStat import StatisticsSolver
import math

class DescriptiveStat(StatisticsSolver): 
      
    def range(self):
        return max(self.data) - min(self.data)
    
    def midrange(self):
        mr = (max(self.data) + min(self.data))/2
        mr = round(mr, self.decimal_places+1)
        return mr
    
    def weighted_mean(self, weights):
        weighted_values = [(self.data[i] * weights[i]) for i in range(len(self.data)-1)]
        weighted_mean = sum(weighted_values)/sum(weights)
        weighted_mean = round(weighted_mean, self.decimal_places + 1)
        return weighted_mean
    
    def z_score(self, x):
        # z actually is how many sd away from the mean 
        z = round((x - self.mean())/self.sd(), 2)
        return z
    
    def percentile_get_p(self, x):
        # percentile is not related to value, only about order/rank
        data.sort()
        i = data.index(x)
        p = (i + 0.5) * 100 / len(data)
        p = round(p)
        return p
    
    def percentile_get_x(self, data, k):
        # given Pk, get x
        # can be performed in R with: quantile(data, probs = 0.4, type = 5)
        data.sort()
        position = k * len(data) / 100
        if position % 1 == 0:
            # plus 0.5 if whole number, equivalent to ...
            position = round(position)
            x = (data[position - 1] + data[position]) / 2
        else:
            # round to next higher whole number
            x = data[math.ceil(position) - 1]
        return x
    
    def quartile_and_more(self, data):
        # this function also follows type 5
        q1 = self.percentile_get_x(data, 25)
        q2 = self.percentile_get_x(data, 50)
        q3 = self.percentile_get_x(data, 75)
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
    
    def a2b_percentile_range(self, data, a, b):
        a, b = (a, b) if a <= b else (b, a)
        pa = self.percentile_get_x(data, a)
        pb = self.percentile_get_x(data, b)
        return pb - pa
    
    def outlier_check(self, data, x):
        q1 = self.percentile_get_x(data, 25)
        q3 = self.percentile_get_x(data, 75)
        iqr = q3 - q1
        status = ''
        if x > (q3 + (3 * iqr)) or x < (q1 - (3 * iqr)):
            status = "a severe outlier"
        elif x > (q3 + (1.5 * iqr)) or x < (q1 - (1.5 * iqr)):
            status = "a mild outlier"
        else:
            status = "not an outlier"
        return status
    
   


