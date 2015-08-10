/**
 * You are given a sequence of words, and a limit on the number of characters
 * that can be put in one line (line width). You need to print the text neatly.
 * i.e. put line breaks in the given sequence of words such that the lines are
 * printed neatly. The condition is that the length of each word should be
 * smaller than the line width.
 *
 * The idea here is to have balanced lines. The extra spaces includes spaces put
 * at the end of every line except the last one. The problem is to minimize the
 * following total cost.
 *
 * Cost of a line = (Number of extra spaces in the line) ^ 3
 * Total cost = Sum of costs for all lines
 *
 * For example, consider the following string and line width M = 15.
 * "Geeks for Geeks presents word wrap problem"
 *
 * Following is the optimized arrangement of words in 3 lines:
 *
 * Geeks for Geeks|
 * presents word  |
 * wrap problem   |
 *
 * The total extra spaces in line 1, line 2 and line 3 are 0, 2 and 3
 * respectively. So optimal value of total cost is 0 + 2*2 + 3*3 = 13.
 */