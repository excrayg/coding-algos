# /**
#  * You are given a sequence of words, and a limit on the number of characters
#  * that can be put in one line (line width). You need to print the text neatly.
#  * i.e. put line breaks in the given sequence of words such that the lines are
#  * printed neatly. The condition is that the length of each word should be
#  * smaller than the line width.
#  *
#  * The idea here is to have balanced lines. The extra spaces includes spaces put
#  * at the end of every line except the last one. The problem is to minimize the
#  * following total cost.
#  *
#  * Cost of a line = (Number of extra spaces in the line) ^ 3
#  * Total cost = Sum of costs for all lines
#  *
#  * For example, consider the following string and line width M = 15.
#  * "Geeks for Geeks presents word wrap problem"
#  *
#  * Following is the optimized arrangement of words in 3 lines:
#  *
#  * Geeks for Geeks|
#  * presents word  |
#  * wrap problem   |
#  *
#  * The total extra spaces in line 1, line 2 and line 3 are 0, 2 and 3
#  * respectively. So optimal value of total cost is 0 + 2*2 + 3*3 = 13.
#  */

#geek for
#geeks


#each word must be kept in all possible lines
def print_neatly(words_list, curr_word_idx, curr_line, rem_spaces_in_curr_line, M):
    if curr_word_idx == 0:
        return (M-len(words_list[curr_word_idx]))**3
        
    if rem_spaces_in_curr_line < len(words_list[curr_word_idx]):
        return rem_spaces_in_curr_line**3
        
    curr_line_cost = (M-len(words_list[curr_word_idx]))**3
                        + print_neatly(words_list, curr_word_idx-1, curr_line, rem_spaces_in_curr_line, M)
                        
    prev_line_cost = print_neatly(words_list, curr_word_idx, curr_line-1, rem_spaces_in_curr_line, M)
    
    
    return min(curr_line_cost, prev_line_cost)
        
    