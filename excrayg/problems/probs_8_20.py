# prob1: given a coin, decide how many times to throw you can get n consecutive head 1/2
n = 1
divergent series or convergent series
-- 1/2 * 1 + 1/2 * 1/2 * 2 + 1/2 * 1/2 * 1/2 *3 +...
i/(2^i) = 0 when i -> infinite
1/2+1/2+1/2.66+1/>2.66
n = 2 
1/2 * 1/2 * 2 + 1/2 * 1/2 *1/2 * 3 + (1/2 * 1/2 *1/2 *1/2 + 1/2 * 1/2 *1/2 *1/2) * 4 +...

E(x) = x*p for all i 

x = 0,1
p = 1/2


1 consecutive head means you see head twice for two coin toss? one toss, one head
throw 2 times 

n consecutive head, 001, n=2 10011
we toss x times, m = x - n - 1, how many combinations  m times without n consecutive heads?
00 10 01
m digits without n consec?
10(m-2)
0(m-1)
(m) = (m - 2) + (m - 1) Fibonacci array
Fm = (m)
x digits 2^x
Fm / 2^x
px = F(x-n-1)/2^x 
expectation = sum(pn to pinfi) = F(n-n-1)/2^n + F(n+1-n-1)/2^(n+1) + F(n+2-n-1)/2^(n+2) ...


n = 1, number of throws is 2

n=1
there are two cases
first case, is head in first throw
second case is tail in first throw and 
y = 1/2 + (1/2 + 1/2*y)
y = 1/2 + 1/2(y+1) = 2+y/2
2y - y = 2
y = 2

n=2
1/4*2 + (1/2 + 1/2*y) + 1/4*2 + 1/4y
y=6

n=3
1/8*3 + (1/2 + 1/2y) + 1/4*2 + 1/4y + 1/8*3 + 1/8y

http://www.wolframalpha.com/input/?i=y%3D1%2F8*3+%2B+%281%2F2+%2B+1%2F2y%29+%2B+1%2F4*2+%2B+1%2F4y+%2B+1%2F8*3+%2B+1%2F8y

n=4

2^(n+1)-2

gambling house : if find someone win n times consecutively 
fair game 
the day the house closes:
n gamblers win
2
4
8
16
...
2^n
2 + 4 + 8 +..2^n = 2^(n + 1) - 2


http://www.matrix67.com/blog/archives/3638
http://jeffe.cs.illinois.edu/teaching/algorithms/


