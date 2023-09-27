import math

def max_decimal_places(nums):
    max_places = 0
    for num in nums:
        if '.' in str(num):
            decimal_places = len(str(num).split('.')[1])
            max_places = max(max_places, decimal_places)
    return max_places
 
def print_dict(d):
    for key, value in d.items():
        print(f'  {key} - {value}')
        

def n_c_x(n, x):
    if x < 0 or x > n:
        return 0
    else:
        return math.comb(n, x)