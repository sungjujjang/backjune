import sys
input = sys.stdin.readline

MAX_num = 0
MAX_sun = 0

for i in range(1, 10):
    N = int(input())
    if MAX_num < N:
        MAX_num = N
        MAX_sun = i
        
print(MAX_num)
print(MAX_sun)
