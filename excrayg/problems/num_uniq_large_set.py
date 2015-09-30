
Problem: try to count unique items of a very large set, say 1TB 64bit integers. You could provide a monte carlo algorithm that just give the approximate result.

#I dont remember what monte carlo algo is off the top of my head. I suppose monte carlo has something to do with randomization.
#1TB - 2^40. Number of 64 bit integers in 1TB. 2^40/2*3 = 2^37
#Worst case, all the numbers in set could be unique. 
#Lets say working memory is 512 MB and I am reading a chunk of set in 256 MB and a dict in 256 MB(2^28). Number of 64 bit integers in 256 MB, 2^25
#we could store a dict in this memory. key - 64 bit, value 64 bit. one [key,val] entry is 2*(2^3) = 2^4 bytes. 
#Number of [key,val] entries in 256 MB, 2^28/2^4 = 2^24 entries. 
#We can process 1TB in chunks of 2^24, count number of uniq items after each chunk pass.

#Time taken: 30 minutes. 

def count_uniq(large_set, set_size):
	#assume a random number generator which gives a random number within a upper bound number. 
	chunk_size = 2^^24
	num_chunks = set_size/chunk_size
	last_chunk_size = set_size%chunk_size
	start_range = 0
	uniq_items = 0
	while num_chunks:
		ctr = 0
		chunk_uniq_dict = defaultdict(int)
		chunk_set = read_from_set(large_set, start_range, chunk_size)
		while ctr < chunk_size:
			idx = rand(chunk_size)
			chosen_elem = chunk_set[idx]
			chunk_uniq_dict[chosen_elem] += 1
			ctr+=1
		uniq_items += find_uniq_items(chunk_uniq_dict) #Iam skipping implementation. Just count items with val == 1
		start_range += chunk_size
		num_chunks -= 1
	
	#Do the above algo for last_chunk_size
	
	return uniq_items
	
		
			