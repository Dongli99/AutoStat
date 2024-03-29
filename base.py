 # This file contains basic statistics functions
import math
from utils import max_decimal_places

class StatisticsSolver:
    def __init__(self, data, is_population = False):
        """
        Initialize the StatisticsSolver object.

        Parameters:
        - data (list): Input dataset.
        - is_population (bool): Flag to indicate whether the dataset represents a population.
        """
        self.data = sorted(data)
        self.is_population = is_population
        self.decimal_places = max_decimal_places(self.data)
        
    def mean(self, is_rounded = True):
        """
        Calculate the mean of the dataset.

        Parameters:
        - decimal_places (int): Number of decimal places to round the result. If None, no rounding.

        Returns:
        - float: Mean value.
        """
        mean = sum(self.data) / len(self.data)
        if is_rounded:
            mean = round(mean, self.decimal_places + 1)
        return mean

    def median(self, is_rounded = True):
        """
        Calculate the median of the dataset.

        Parameters:
        - decimal_places (int): Number of decimal places to round the result. If None, no rounding.

        Returns:
        - float: Median value.
        """
        self.data.sort()
        n = len(self.data)
        if n%2 == 0:
            median = (self.data[n//2-1] + self.data[n//2])/2
            if is_rounded:
                median = round(median, self.decimal_places + 1)
        else:
            median = self.data[(n-1)//2]
        return median
    
    def mode(self):
        """
        Calculate the mode of the dataset.

        Returns:
        - str or list: Mode value(s) or "No mode".
        """
        frequency_dict = {}
        for num in self.data:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        max_frequency = max(frequency_dict.values())
        mode_values = [num for num, frequency in frequency_dict.items() if frequency == max_frequency]
        
        if max_frequency == 1 or len(mode_values) == len(self.data):
            return "No mode"
        elif len(mode_values) == 1:
            return mode_values[0]
        else:
            return mode_values
    
    def variance(self, is_rounded = True):
        """
        Calculate the variance of the dataset.

        Parameters:
        - decimal_places (int): Number of decimal places to round the result. If None, no rounding.

        Returns:
        - float: Variance value.
        """    
        var_list = [(x-self.mean())**2 for x in self.data]
        variance = sum(var_list) / len(self.data) if self.is_population else sum(var_list)/(len(self.data)-1)
        if is_rounded:
            variance = round(variance, self.decimal_places + 1)
        return variance
    
    def standard_deviation(self, is_rounded = True):
        """
        Calculate the standard deviation of the dataset.

        Parameters:
        - decimal_places (int): Number of decimal places to round the result. If None, no rounding.

        Returns:
        - float: Standard deviation value.
        """
        sd = math.sqrt(self.variance(False))
        if is_rounded:
            sd = round(sd, self.decimal_places + 1)
        return sd
    
    def range(self):
        """
        Calculate the range of the dataset.

        Returns:
        - float: Range value.
        """
        return self.data[-1] - self.data[0]