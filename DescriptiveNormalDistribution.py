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
        self.z_df.columns = self.z_df.iloc[0].astype(int)
        # create index array
        self.rows = [-340, -330, -320, -310, -300, -290, -280, -270, -260, -250, -240, -230, -220, -210, -200, -190, -180, -170, -160, -150, -140, -130, -120, -110, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340]
        self.cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def z_score_lookup_lower(self, num):

        # split number into two 
        row_v, col_v = split_number(num)
        row_i = self.rows.index(row_v)
        if row_v == 0 and num >= 0:
            row_i += 1
        col_i = self.cols.index(col_v)
        # query the data frame
        return self.z_df.iloc[row_i, col_i]
    
    def z_score_lookup_greater(self,num):
        return 1-self.z_score_lookup_lower(num)
    
    def z_score_lookup_between(self, bottom, top):
        return self.z_score_lookup_lower(top) - self.z_score_lookup_lower(bottom)
            
    def lower_than_z0(self, value):
        diff = 1000000
        tie = False
        # loop to get the index of value
        for i in range(len(self.rows)):
            for j in range(len(self.cols)):
                if value - self.z_df.iloc[i, j] > diff:
                    if j == 0:
                        row_i = i-1
                        col_i = 9
                    else:
                        row_i = i
                        col_i = j-1
                    break
                elif value - self.z_df.iloc[i, j] == diff:
                    tie = True
                    if j == 0:
                        row_i = [i-1, i]
                        col_i = [9, 0]
                    else:
                        row_i = [i, i]
                        col_i = [j-1, j]
                    break
                else:
                    diff = value - self.z_df.iloc[i, j]
        if tie:
            row_v1, col_v1 = self.rows[row_i[0]], self.cols[col_i[0]]
            row_v2, col_v2 = self.rows[row_i[1]], self.cols[col_i[1]]
            v1 = row_v1 + col_v1
            v2 = row_v2 + col_v2
            v = (v1+v2)/200 
        else:
            v = (self.rows[row_i] + self.cols[col_i])/100
        return v
            
            

                
        
        
        
        
        
        
        
                  