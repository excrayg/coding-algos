
#A Pair with the Maximal Difference

#Problem: A pair contains two numbers, and its second number is on the right side of the first one in an array. The difference of a pair is the minus result while subtracting the second number from the first one. Please implement a function which gets the maximal difference of all pairs in an array. For example, the maximal difference in the array {2, 4, 1, 16, 7, 5, 11, 9} is 11, which is the minus result of pair (16, 5).

# 1, 2, 4, 5, 7, 9, 11, 16
# 2, 0, 1, 5, 4, 7, 6, 3.

#Sort the array. keeping in track of the original indexes. find first i > j, i starts from beginning of array. j is end of array. 

def max_diff(numbers):
	number_idx_tuples_list = []
	for idx, elem in enumerate(numbers):
		number_idx_

