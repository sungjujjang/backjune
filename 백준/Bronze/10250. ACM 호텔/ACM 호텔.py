import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

num = int(input())
 
for i in range(num):
    H, W, N = map(int, input().split())
    f = N % H
    r = N // H + 1
    if f == 0:
        r -= 1
        f = H
 
    print(f*100 + r)