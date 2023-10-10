# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 08:52:32 2023

@author: Dongli
"""
from utils import split_number
import pandas as pd

class DescriptiveNormalDistribution:
    
    def __init__(self):
        # import .csv and prepare data frame.
        self.z_df = pd.read_csv('zscore.csv', index_col=0)
        self.z_df.iloc[0] = self.z_df.iloc[0].fillna(0)
        self.z_df.columns = self.z_df.iloc[0].astype(int)
        # create index array
        self.rows = [-340, -330, -320, -310, -300, -290, -280, -270, -260, -250, -240, -230, -220, -210, -200, -190, -180, -170, -160, -150, -140, -130, -120, -110, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340]
        self.cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def get_pvalue_zlower(self, num):

        # split number into two 
        row_v, col_v = split_number(num)
        row_i = self.rows.index(row_v)
        if row_v == 0 and num >= 0:
            row_i += 1
        col_i = self.cols.index(col_v)
        # query the data frame 
        return self.z_df.iloc[row_i, col_i]
    
    def get_pvalue_zgreater(self,num):
        return round(1-self.get_pvalue_zlower(num), 4)
    
    def get_pvalue_zbetween(self, bottom, top):
        return round(self.get_pvalue_zlower(top) - self.get_pvalue_zlower(bottom), 4)
            
    def _lower_than_z0(self, value):
        diff = 1000000
        tie = False
        row_i = None
        col_i = None
        # loop to get the index of value
        for i in range(len(self.rows)):
            for j in range(len(self.cols)):
                current_diff = value - self.z_df.iloc[i, j]
                if current_diff == 0:
                    row_i = i
                    col_i = j
                    break
                elif current_diff < 0:
                    if abs(current_diff) <= diff:
                        if abs(current_diff) == diff:
                            tie = True
                        row_i = i
                        col_i = j
                    else:
                        if j == 0:
                            row_i = i-1
                            col_i = 9
                        else:
                            row_i = i-1
                            col_i = j-1
                    break
                else:
                    diff = current_diff
            if row_i is not None:
                break
        row_v = self.rows[row_i]
        col_v = self.cols[col_i]
        v = (row_v + col_v)/100 if value >= 0.5 else (row_v - col_v)/100
        if tie:
            v = v - 0.005
        return v
    
    def lower_than_z0(self, value):
        is_negtive = True if value<0.5 else False
        if is_negtive:
            return - self._lower_than_z0(1-value)
        return self._lower_than_z0(value)
            

                
        
        
        
        
        
        
        
                  