import math

def max_decimal_places(nums):
    """
    Calculates the maximum number of decimal places among a list of numbers.

    Args:
        nums (list): List of numbers.

    Returns:
        int: Maximum number of decimal places.
    """
    max_places = 0
    for num in nums:
        if '.' in str(num):
            decimal_places = len(str(num).split('.')[1])
            max_places = max(max_places, decimal_places)
    return max_places
 
def print_dict(d):
    """
    Prints key-value pairs of a dictionary in a formatted way.

    Args:
        d (dict): Dictionary to be printed.
    """
    for key, value in d.items():
        print(f'  {key} - {value}')
        

def n_c_x(n, x):
    """
    Calculates the binomial coefficient "n choose x" (nCx).

    Args:
        n (int): Total number of items.
        x (int): Number of items to choose.

    Returns:
        int: Binomial coefficient value.
    """
    if x < 0 or x > n:
        return 0
    else:
        return math.comb(n, x)
    
def split_number(num):
    """
    Splits a number into its left and right parts.

    Args:
        num (float): Input number.

    Returns:
        tuple: Tuple containing the left and right parts.
    """
    # e.g. given (+/-)3.41, output (+/-)340 and 1
    is_positive = True if num>=0 else False
    num = abs(num) * 100
    num_right = round(num % 10)
    num_left = round(num - num_right)
    if not is_positive:
        num_left = 0-num_left
    return num_left, num_right

def z_score(x, mean, sd):
    """
    Calculates the z-score for a given value, mean, and standard deviation.

    Args:
        x (float): Input value.
        mean (float): Mean of the distribution.
        sd (float): Standard deviation of the distribution.

    Returns:
        float: Z-score.
    """
    return round((x - mean) / sd, 2)

