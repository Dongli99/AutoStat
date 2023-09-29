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
    
def split_number(num):
    # e.g. given (+/-)3.41, output (+/-)340 and 1
    is_positive = True if num>=0 else False
    num = abs(num) * 100
    num_right = round(num % 10)
    num_left = round(num - num_right)
    if not is_positive:
        num_left = 0-num_left
    return num_left, num_right

