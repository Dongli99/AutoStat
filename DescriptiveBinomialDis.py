# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:47:35 2023

@author: Dongli
"""
from utils import n_c_x
import math

class DescriptiveBinomialDis:
    
    def __init__(self, p, n, x=0):
        self.n = n
        self.x = x
        self.p = p
        self.q = 1-p
    
    def binomial_probability(self, is_rounded = True):
        p_x = n_c_x(self.n, self.x) * math.pow(self.p, self.x) * math.pow(self.q, self.n-self.x)
        if is_rounded:
            p_x = round(p_x, 3)
        return p_x
    
    def bino_prob_sum(self, bottom, top, is_rounded = True):
        x = bottom
        probs = 0
        while x <= top:
            self.x = x
            probs += self.binomial_probability(False)
            x += 1
        if is_rounded:
            probs = round(probs,3)
        return probs
    
    def bino_prob_mean(self, is_rounded = True):
        mean = 0
        for x in range(self.n+1):
            self.x = x
            mean += self.binomial_probability(False) * x
        if is_rounded:
            mean = round(mean, 3)
        return mean
    
    def bino_prob_variance(self, is_rounded = True):
        v = 0
        for x in range(self.n+1):
            self.x = x
            v += self.binomial_probability(False) * x**2
        v = v - self.bino_prob_mean(False)**2        
        if is_rounded:
            v = round(v, 3)
        return v
    
    def bino_prob_sd(self, is_rounded = True):
        sd = math.sqrt(self.bino_prob_variance(False))
        if is_rounded:
            sd = round(sd, 3)
        return sd
    
    def expect_success(self, is_rounded = True):
        ex = self.n * self.p
        if is_rounded:
            ex = round(ex, 1)
        return ex