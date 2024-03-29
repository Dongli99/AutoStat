# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 10:11:15 2023

@author: Dongli
"""
from base import StatisticsSolver
import math

class DescriptiveStat(StatisticsSolver): 

    def range(self):
        """
        Calculate the range of the dataset.

        Returns:
        - float: Range value.
        """
        return max(self.data) - min(self.data)
    
    def midrange(self, is_rounded = True):
        """
        Calculate the midrange of the dataset.

        Parameters:
        - is_rounded (bool): Flag to indicate whether to round the result.

        Returns:
        - float: Midrange value.
        """
        mr = (max(self.data) + min(self.data))/2
        if is_rounded:
            mr = round(mr, self.decimal_places+1)
        return mr
    
    def weighted_mean(self, weights, is_rounded = True):
        """
        Calculate the weighted mean of the dataset.

        Parameters:
        - weights (list): Weights for each data point.
        - is_rounded (bool): Flag to indicate whether to round the result.

        Returns:
        - float: Weighted mean value.
        """
        weighted_values = [(self.data[i] * weights[i]) for i in range(len(self.data)-1)]
        weighted_mean = sum(weighted_values)/sum(weights)
        if is_rounded:
            weighted_mean = round(weighted_mean, self.decimal_places + 1)
        return weighted_mean
    
    def _z_score(self, x):
        """
        Calculate the z-score of a value.

        Parameters:
        - x (float): Value for which to calculate the z-score.

        Returns:
        - float: Z-score value.
        """
        return round((x - self.mean(False))/self.standard_deviation(False), 2)
    
    def z_score(self, x, mean, sd):
        """
        Calculate the z-score of a value using external mean and standard deviation.

        Parameters:
        - x (float): Value for which to calculate the z-score.
        - mean (float): Mean of the dataset.
        - sd (float): Standard deviation of the dataset.

        Returns:
        - float: Z-score value.
        """
        return round((x - mean) / sd, 2)
    
    def percentile_get_p(self, x):
        """
        Calculate the percentile rank of a value.

        Parameters:
        - x (float): Value for which to calculate the percentile rank.

        Returns:
        - float: Percentile rank value.
        """
        # percentile is not related to value, only about order/rank
        return round((self.data.index(x) + 0.5) * 100 / len(self.data))
    
    def percentile_get_x(self, k):
        """
        Calculate the value at a given percentile rank.

        Parameters:
        - k (float): Percentile rank.

        Returns:
        - float: Value at the given percentile rank.
        """
        # given Pk, get x
        # can be performed in R with: quantile(data, probs = 0.4, type = 5)
        position = k * len(self.data) / 100
        if position % 1 == 0:
            # plus 0.5 if whole number, equivalent.
            position = round(position)
            x = round((self.data[position - 1] + self.data[position]) / 2, self.decimal_places+1)
        else:
            # round to next higher whole number
            x = self.data[math.ceil(position) - 1]
        return x
    
    def quartile_and_more(self):
        """
        Calculate quartiles and related statistics.

        Returns:
        - dict: Dictionary containing quartile and related statistics.
        """
        # this function also follows type 5
        q1 = self.percentile_get_x(25)
        q2 = self.percentile_get_x(50)
        q3 = self.percentile_get_x(75)
        iqr = q3 - q1
        semi_iqr = iqr / 2
        mid_quartile = round((q1 + q3) / 2, self.decimal_places+1)
        mild_boundary = [round(q1-(1.5*iqr), self.decimal_places+1), round(q3+(1.5*iqr), self.decimal_places+1)]
        extreme_boundary = [round(q1-(3*iqr), self.decimal_places+1), round(q3+(3*iqr), self.decimal_places+1)]
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
        """
        Calculate the range between two percentiles.

        Parameters:
        - a (float): Lower percentile.
        - b (float): Upper percentile.

        Returns:
        - float: Range between the two percentiles.
        """
        # calculate the range between 2 percentiles
        a, b = (a, b) if a <= b else (b, a)
        pa = self.percentile_get_x(a)
        pb = self.percentile_get_x(b)
        return pb - pa
    
    def outlier_check(self, x):
        """
        Check if a value is an outlier.

        Parameters:
        - x (float): Value to check.

        Returns:
        - str: Outlier status.
        """
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
            