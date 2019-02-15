'''
If we list all the natural numbers below 10 that are multiples of 3 or 5 , we get 3, 5, 6, and 9. 
The sum of these multiples is 23 .

Find the sum of all the multiples of 3 or 5 below N .

Input Format

First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N .

Constraints 1 ≤ T ≤ 10^5 1 ≤ N ≤ 10^9

Output Format

For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below . N

SAMPLE INPUT 
2
10
100
SAMPLE OUTPUT 
23
2318
'''

t=int(input())
for i in range(t):
    n=int(input())
    s=0
    for j in range(1,n):
        if j%3==0 or j%5==0:
            s+=j
    print(s)
