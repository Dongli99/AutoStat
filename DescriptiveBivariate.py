# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:39:08 2023

@author: Dongli
"""
from base import StatisticsSolver
import math

class DescriptiveBivariate:
    
    def __init__(self, x_list, y_list):
        """
        Initialize the DescriptiveBivariate class.

        Parameters:
        - x_list (list): List of x-values.
        - y_list (list): List of y-values.
        """
        self.x_list = x_list
        self.y_list = y_list
        self.x_y_list = [[x, y] for x, y in zip(self.x_list, self.y_list)]
        self.mean_x = StatisticsSolver(self.x_list).mean(False)
        self.mean_y = StatisticsSolver(self.y_list).mean(False)
        self.sd_x = StatisticsSolver(self.x_list).standard_deviation(False)
        self.sd_y = StatisticsSolver(self.y_list).standard_deviation(False)
        
    def linear_regression(self):
        """
        Perform linear regression on the given data.

        Returns:
        - dict: Dictionary containing slope (m), intercept (b), and the linear regression formula.
        """
        # will create liniea regression line
        # get m
        sum_x = sum(self.x_list)
        sum_y = sum(self.y_list)
        sum_xy = sum(x * y for x, y in zip(self.x_list, self.y_list))
        sum_x_sq = sum(x * x for x in self.x_list)
        n = len(self.x_list)
        m = (n * sum_xy - (sum_x * sum_y)) / (n * sum_x_sq - (sum_x * sum_x))
        # get b
        b = self.mean_y - (m * self.mean_x)
        # return result
        m = round(m, 3)
        b = round(b, 3)
        line = {'m: ': m, 'b: ': b, 'formula: ': f'y^ = {m}x + {b}'}
        return line
    
    def correlation_coefficient(self, is_rounded = True):
        """
        Calculate the correlation coefficient (Pearson's r).

        Parameters:
        - is_rounded (bool): Flag to indicate whether to round the result.

        Returns:
        - float: Correlation coefficient.
        """
        # the closer the value to -1 or 1, the stronger the correlation. 0 - no correlation
        sum_x = sum(self.x_list)
        sum_y = sum(self.y_list)
        sum_xy = sum(x * y for x, y in zip(self.x_list, self.y_list))
        sum_x_sq = sum(x * x for x in self.x_list)
        sum_y_sq = sum(y * y for y in self.y_list)
        n = len(self.x_list)
        numerator = n * sum_xy - sum_x * sum_y
        denominator = math.sqrt((n * sum_x_sq - sum_x**2) * (n * sum_y_sq - sum_y**2))
        r = numerator / denominator
        if is_rounded:
            r = round(r, 3)
        return r
    
    def coefficient_of_determination(self, is_rounded = True):
        """
        Calculate the coefficient of determination (r-squared).

        Parameters:
        - is_rounded (bool): Flag to indicate whether to round the result.

        Returns:
        - float: Coefficient of determination.
        """
        # a better measure when we decide about the linearity of a relationship 
        # the proportion of variation in the y values that is explained by x
        cd = self.correlation_coefficient(False)**2
        if is_rounded:
            cd = round(cd, 3)
        return cd