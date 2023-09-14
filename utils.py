def max_decimal_places(self, nums):
    max_places = 0
    for num in nums:
        if '.' in str(num):
            decimal_places = len(str(num).split('.')[1])
            max_places = max(max_places, decimal_places)
    return max_places
 
def print_dict(self, d):
    for key, value in d.items():
        print(f'  {key} - {value}')