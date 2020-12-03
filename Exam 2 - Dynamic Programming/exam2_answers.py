import numpy as np
import math

def print_dp(dp):
    for row in dp:
        print(row)
    print()

def minimum_fall_path_sum(A):
    if len(A)==0:
        return 0
    rows,cols=len(A),len(A[0])
    dp = [[0]*cols for i in range(rows-1)] 
    dp.insert(0,A[:1][:]) # Inserts A[0][:] to dp[0][:], values of first row
    for r in range(1,rows):
        for c in range(cols):
            down = A[r][c]
            left = math.inf if c-1<0 else A[r][c-1] # avoid index out-of-bounds
            right = math.inf if c+1>=cols else A[r][c+1] # avoid index out-of-bounds
            dp[r][c] += min(left,down,right) + A[r-1][c] # get min(l,d,r) + prev computations from top (cumulative sum)
    print_dp(dp)
    return np.min(dp[-1:][:]) # Get minimum fall path (cumulative) sum

def arithmetic_slices(A):
    n = len(A)
    dp=[0]*n
    for i in range(2,n):
        if A[i]-A[i-1]==A[i-1]-A[i-2]: # Valid arithmetic sequence
            dp[i]= dp[i-1]+1
    cumulative=0
    for i in range(n):
        cumulative+=dp[i] # Sum the backtrack sum.
    return cumulative

def min_ascii_del_sum(s1,s2):
    n1,n2=len(s1)+1,len(s2)+1
    dp=[[0]*n2 for _ in range(n1)]
    for c in range(1,n2):
        dp[0][c]=dp[0][c-1]+ord(s2[c-1]) # Fill first row
    for c in range(1,n1):
        dp[c][0]=dp[c-1][0]+ord(s1[c-1]) # Fill first column
    for r in range(1,n1):
        for c in range(1,n2):
            if s1[r-1]==s2[c-1]: # Characters match, grab the top left value.
                dp[r][c]=dp[r-1][c-1]
            else: # Mismatch, grab the minimum 2 prev computation (left and top), min(left+s2[r-1],top+s1[c-1]) 
                dp[r][c]=min(dp[r-1][c]+ord(s1[r-1]), 
                             dp[r][c-1]+ord(s2[c-1]))
    return dp[-1][-1]

print(minimum_fall_path_sum([[1,2],[4,5]]))
print(minimum_fall_path_sum([[1,2,3],[4,5,6],[7,8,9]]))
print(minimum_fall_path_sum([[0,1,0],[3,0,3],[9,5,2]]))

print(arithmetic_slices([1,3,5,7,9]))
print(arithmetic_slices([1,2,3,4]))
print(arithmetic_slices([1,2,3,4,5]))
print(arithmetic_slices([1,3,5,8,10]))

print(min_ascii_del_sum('',''))
print(min_ascii_del_sum('e','e'))
print(min_ascii_del_sum('','a'))
print(min_ascii_del_sum('e','a'))
print(min_ascii_del_sum('ee','a'))
print(min_ascii_del_sum('eat','sea'))
print(min_ascii_del_sum('delete','leet'))
