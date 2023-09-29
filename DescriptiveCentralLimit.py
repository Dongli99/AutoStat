# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 00:00:26 2023

@author: Dongli
"""
import math
from DescriptiveNormalDistribution import DescriptiveNormalDistribution


class DescriptiveCentralLimit(DescriptiveNormalDistribution):
    def __init__(self, mean_p, sd_p, sample_size):
        super().__init__()
        self.n = sample_size
        self.mean_p = mean_p
        self.sd_p = sd_p
        self.mean_s = mean_p
        self.sd_s = sd_p / (math.sqrt(self.n))
       
    def get_p_value_lower(self, x):
        z = (x - self.mean_s)/self.sd_s
        return self.get_pvalue_zlower(z)
    
    def get_p_value_greater(self, x):
        z = (x - self.mean_s)/self.sd_s
        return self.get_pvalue_zgreater(z)
    
    def get_p_value_between(self, bottom, top):
        z1 = (bottom - self.mean_s)/self.sd_s
        z2 = (top - self.mean_s)/self.sd_s
        return self.get_pvalue_zbetween(z1, z2)
    
    
        
    