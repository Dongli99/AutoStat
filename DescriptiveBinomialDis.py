# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:47:35 2023

@author: Dongli
"""
from utils import n_c_x
import math

class DescriptiveBinomialDis:
    
    def __init__(self, n, x, p):
        self.n = n
        self.x = x
        self.p = p
        self.q = 1-p
    
    def binomial_probability(self, is_rounded = True):
        p_x = n_c_x(self.n, self.x) * math.pow(self.p, self.x) * math.pow(self.q, self.n-self.x)
        if is_rounded:
            p_x = round(p_x, 3)
        return p_x
    
