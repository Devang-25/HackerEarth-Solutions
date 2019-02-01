'''
Given A and B, count the numbers N such that A ≤ N ≤ B and N is a palindrome.

Examples: 
Palindromes: 121, 11 , 11411 
Not Palindromes: 122, 10

Input: 
First line contains T, the number of testcases. Each testcase consists of two integers A and B in one line.

Output: 
For each testcase, print the required answer in one line.

Constraints: 
1 ≤ T ≤ 10 
0 ≤ A ≤ B ≤ 105

SAMPLE INPUT 
2
10 13
20 30
SAMPLE OUTPUT 
1
1
'''
t=int(input())
for i in range(t):
    s=[int(x) for x in input().split(" ")]
    cnt=0
    for j in range(s[0],s[1]+1):
        if str(j)==str(j)[::-1]:
            cnt+=1
    print(cnt)
