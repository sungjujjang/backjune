import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
for i in range(0, n):
    a, b = input().split()
    for c in b:
        print(c*int(a), end="")
    print()
