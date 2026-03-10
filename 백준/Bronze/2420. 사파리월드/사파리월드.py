import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

if n > m:
    print(n-m)
else:
    print(m-n)