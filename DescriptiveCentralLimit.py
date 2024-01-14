# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 00:00:26 2023

@author: Dongli
"""
import math
from DescriptiveNormalDistribution import DescriptiveNormalDistribution


class DescriptiveCentralLimit(DescriptiveNormalDistribution):
    def __init__(self, mean_p, sd_p, sample_size):
        """
        Initialize the DescriptiveCentralLimit class.

        Parameters:
        - mean_p (float): Population mean.
        - sd_p (float): Population standard deviation.
        - sample_size (int): Size of the sample.
        """
        super().__init__()
        self.n = sample_size
        self.mean_p = mean_p
        self.sd_p = sd_p
        self.mean_s = mean_p
        self.sd_s = sd_p / (math.sqrt(self.n))
       
    def get_p_value_lower(self, x):
        """
        Get the p-value for a given value x (lower tail).

        Parameters:
        - x (float): Value to compute the p-value for.

        Returns:
        - float: p-value.
        """
        z = (x - self.mean_s)/self.sd_s
        return self.get_pvalue_zlower(z)
    
    def get_p_value_greater(self, x):
        """
        Get the p-value for a given value x (upper tail).

        Parameters:
        - x (float): Value to compute the p-value for.

        Returns:
        - float: p-value.
        """
        z = (x - self.mean_s)/self.sd_s
        return self.get_pvalue_zgreater(z)
    
    def get_p_value_between(self, bottom, top):
        """
        Get the p-value for a range of values [bottom, top].

        Parameters:
        - bottom (float): Bottom value of the range.
        - top (float): Top value of the range.

        Returns:
        - float: p-value.
        """
        z1 = (bottom - self.mean_s)/self.sd_s
        z2 = (top - self.mean_s)/self.sd_s
        return self.get_pvalue_zbetween(z1, z2)
    
    
        
    