import sys
import math

input = sys.stdin.readline

memo = [-1] * 101

def fibo(n):	
    if n == 1 or n == 2:
        return 1
    if memo[n] == -1:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = int(input())
print(fibo(n))