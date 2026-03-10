import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

input()
a = list(map(int, input().split()))
print(min(a), max(a))