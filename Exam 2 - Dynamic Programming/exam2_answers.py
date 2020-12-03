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

print(minimum_fall_path_sum([[1,2],[4,5]]))
print(minimum_fall_path_sum([[1,2,3],[4,5,6],[7,8,9]]))
print(minimum_fall_path_sum([[0,1,0],[3,0,3],[9,5,2]]))
