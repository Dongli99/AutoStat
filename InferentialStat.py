# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:14:56 2023

@author: Dongli
"""
import math
import pandas as pd
from Descriptive import DescriptiveStat
from DescriptiveNormalDistribution import DescriptiveNormalDistribution

class InferentialStat(DescriptiveStat, DescriptiveNormalDistribution):
    
    def init(self, mean, ci, sample_size, is_population):
        """
        Initialize the InferentialStat class.

        Parameters:
        - mean (float): Mean of the data.
        - ci (float): Confidence interval.
        - sample_size (int): Sample size.
        - is_population (bool): Whether the data represents a population or a sample.
        """
        self.significance = ( 1 - ci )
        self.n = sample_size
        self.ci = ci
        # according to sample mean or population mean, give different calculation
        if is_population:
            self.mean_p = mean
            self.criticle_value = self.get_pvalue_zlower(self.significance/2)
            self.margin_error = self.get_margin_error(self.criticle_value, self.n, self.main_p)
        else:
            self.mean_s = mean
            self.criticle_value = self.get_t_value(self.n, self.ci)
            self.margin_error = self.get_margin_error(self.criticle_value, self.n, self.main_s)
    
    def get_t_value(self, n, ci):
        """
        Get the t-value for a given sample size and confidence interval.

        Parameters:
        - n (int): Sample size.
        - ci (float): Confidence interval.

        Returns:
        - float: t-value.
        """
        # read t value table to check the value
        degree_of_freedom = n-1
        df = pd.read_csv('ttable.csv')
        if ci not in df.columns:
            return 'confidence interval not found'
        degrees = df.iloc[:, 0].tolist()
        row_index = 0
        for i in range(len(degrees)):
            if degrees[i] <= degree_of_freedom:
                row_index = i
            else:
                break
        col_index = df.columns.get_loc(ci)
        return df.icol[row_index, col_index]
        
    def set_confidence_interval(self, bottom, top):
        """
        Set the confidence interval.

        Parameters:
        - bottom (float): Lower bound of the confidence interval.
        - top (float): Upper bound of the confidence interval.
        """
        self.ci_low = bottom
        self.ci_high = top
        
    
    def get_margin_error(self, criticle_value, n, main):
        """
        Calculate the margin of error.

        Parameters:
        - criticle_value (float): Critical value.
        - n (int): Sample size.
        - main (float): Mean.

        Returns:
        - float: Margin of error.
        """
        return criticle_value * main / math.sqrt(n)
        
    