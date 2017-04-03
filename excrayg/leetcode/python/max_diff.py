
#A Pair with the Maximal Difference

#Problem: A pair contains two numbers, and its second number is on the right side of the first one in an array. The difference of a pair is the minus result while subtracting the second number from the first one. Please implement a function which gets the maximal difference of all pairs in an array. For example, the maximal difference in the array {2, 4, 1, 16, 7, 5, 11, 9} is 11, which is the minus result of pair (16, 5).

# 1, 2, 4, 5, 7, 9, 11, 16
# 2, 0, 1, 5, 4, 7, 6, 3.

#20,30,99,100
#1,2,0,3
#0,1,2,3

#1,2,3,4
#0,1,2,3

#0,3 - else condition, 1,3 or 0,2 

#Sort the array. keeping in track of the original indexes. find first idx[i] > idx[j], i starts from beginning of array. j is end of array. 

# def max_diff(numbers):
# 	number_idx_tuples_list = []
# 	for idx, elem in enumerate(numbers):
# 		number_idx_tuples_list.append((elem,idx))
# 	sorted(number_idx_tuples_list, key=lambda x: x[0])
# 	n = len(number_idx_tuples_list)
# 	i = 0
# 	j = n-1
	
# 	while i > j:
# 		li = number_idx_tuples_list[i][1]
# 		ri = number_idx_tuples_list[j][1]
# 		if li > ri:
# 			break
# 		else:
# 			if i-j>1:
# 				ln = numbers[li]
# 				rn = numbers[ri]
# 				ln_1 = number_idx_tuples_list[i+1][1]
# 				rn_1 = number_idx_tuples_list[j-1][1]
				
# 				if ln - rn_1 > ln_1 - rn:
# 					i+=1
# 				else:
# 					j-=1
				
# 			else:
# 				break
				
# 	return number_idx_tuples_list[j][0] - number_idx_tuples_list[i][0]

#correct solution

l = [2, 4, 1, 16, 7, 5, 11, 9]

min_elem = float("inf")
max_diff = float("-inf")

i = len(l)-1
while i >= 0:
	min_elem = min(l[i], min_elem)
	max_diff = max(l[i]-min_elem, max_diff)
	i-=1
print(max_diff)

# good work!
