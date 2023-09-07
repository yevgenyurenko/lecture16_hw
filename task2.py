class Mathematician:  
    def square_nums(self, list_nums):
        return [num**2 for num in list_nums]
    
    def remove_positives(self, list_nums):
        non_positive_nums = []
        try:
            for i in list_nums:
                if i <= 0:
                    non_positive_nums.append(i)
        except TypeError:
            print("Input list contains non-numeric elements.")
        return non_positive_nums
    
    def filter_leaps(self, list_nums):
        leap_years = []
        for i in list_nums:
            if (i % 4 == 0) and not (i % 100 == 0) or (i % 400 == 0):
                leap_years.append(i)
        return leap_years

m = Mathematician()

assert m.square_nums([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
assert m.remove_positives([-2, 4, -6, 8, -10]) == [-2, -6, -10]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

print("All assertions passed!")
